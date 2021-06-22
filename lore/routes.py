import datetime
import uuid
from functools import wraps

from flask import Blueprint, request, make_response, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import ValidationError
import jwt
from flask_socketio import join_room, emit, send

api = Blueprint('api', __name__)

from lore import db, socketio
from lore.models.schema import *

def validate_user(user_id, document_id):
    pass

@socketio.event
def connect():
    print("Connected")

@socketio.on('get-document')
def get_document(data):
    # print(f"GET DOCUMENT: req: {data}")
    user = data['user'] # Validate user
    join_room(data['document'])
    doc = Paragraph.get(data['document'])
    # print(doc.body)
    emit('load-document', doc.body)

@socketio.on('send-changes')
def send_changes(data, **kwargs):
    # print(f"SEND CHANGES: req: {data}")
    emit('receive-changes', data['delta'], broadcast=True, include_self=False, room=data['document'])

@socketio.on('save-document')
def save_document(data, **kwargs):
    doc = data['delta']['ops'][0]['insert']
    print(doc)
    # pass
    #print(f"SAVE-DOCUMENT: req: {data}")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return {'message': 'Token is missing'}
        try:
            data = jwt.decode(token, api.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return {'message':'Invalid token'}
        
        return f(current_user, *args, **kwargs)
    return decorated

def build_response(message, code=200, obj=None, sch=None):
    ret = {'message': message}
    if obj is not None and sch is not None:
        ret['obj'] = sch.dump(obj)
    return ret, code

def get_all(obj, sch, endpoint, paginate=False):
    try:
        if paginate:
            page = request.args.get('page',1,type=int)
            per_page = request.args.get('per_page',20,type=int)
            ref = obj.query.paginate(page, per_page, False)
            output = {
                'items': sch.dump(ref.items),
                '_meta': {
                    'page': page,
                    'per_page': per_page,
                    'total_pages': ref.pages,
                    'total_items': ref.total
                },
                '_links': {
                    'self': request.full_path,
                    'next': url_for(f'api.{endpoint}', 
                        page=page+1, per_page=per_page) if ref.has_next else None,
                    'prev': url_for(f'api.{endpoint}', 
                        page=page-1, per_page=per_page) if ref.has_prev else None,
                }
            }
        else:
            ref = obj.query.all()
            output = {'items': sch.dump(ref),
                      '_links': {'self': request.full_path}
                     }
        return output #sch.dump(obj.query.all())
    except Exception as e:
        print(str(e))
        return build_response(f"error {str(e)}", 500)

def get_one(obj, sch, pk, **kwargs):
    try: 
        if stub := kwargs.get('stub', None):
            o = obj.query.filter_by(stub=stub).first()
        else:
            o = obj.query.get(pk)
        if not o:
            return build_response('no such object', 404)
        return sch.dump(o)
    except Exception as e:
        print(str(e))
        return build_response(f"error {str(e)}", 500)
def remove(obj, sch, pk):
    try:
        o = obj.query.get(pk)
        if o is None:
            return build_response(f"no such object", 404)
        db.session.remove(o)
        db.session.commit()
        return build_response(f"removed id:{pk}")
    except ValidationError as e:
        return build_response(f"invalid data", 400)
    except Exception as e:
        return build_response(f"error: {str(e)}", 500)
def create(obj, sch):
    try:
        data = request.get_json()
        o = obj(**sch.load(data=data))
        db.session.add(o)
        db.session.commit()
        return build_response(f"added: {sch.dumps(o)}")
    except Exception as e:
        return build_response(f"error: {str(e)}", 500)
def update(obj, sch, pk):
    try:
        data = request.get_json()
        o = obj.query.get(pk)
        for key, val in sch.load(data=data).items():
            setattr(o, key, val)
        db.session.add(o)
        db.session.commit()
        return build_response(f"updated id:{pk}")
    except Exception as e:
        return build_response(f"error: {str(e)}", 500)

## User endpoints

@api.get('/user')
def get_users():
    return get_all(User, users_schema, 'get_users')

@api.get('/user/<int:pk>')
def get_user(pk):
    return get_one(User, user_schema, pk)

@api.post('/user')
def new_user():
    return create(User, user_schema)

@api.delete('/user/<int:pk>')
def remove_user(pk):
    return remove(User, user_schema, pk)

@api.put('/user/<int:pk>')
def update_user(pk):
    return update(User, user_schema, pk)

## Page endpoints

@api.get('/page')
def get_pages():
    return get_all(Page, pages_schema, 'get_pages', paginate=True)

@api.get('/page/<int:pk>')
def get_page(pk):
    return get_one(Page, page_schema, pk)

@api.get('/page/<int:pk>/paragraphs')
def get_page_paragraphs():
    return ""


@api.get('/page/stub/<string:stub>')
def get_page_by_stub(stub):
    return get_one(Page, page_schema, 0, stub=stub)

@api.put('/page/<int:pk>/set_parent')
def set_parent_page(pk):
    try:
        this = Page.get(pk)
        data = request.get_json()
        parent_id = data.parent_id
        parent = Page.get(parent_id)
        this.set_parent(parent)
    except Exception as e:
        return build_response(f'invalid request, {str(e)}', 400)

@api.post('/page')
def new_page():
    return create(Page, page_schema)

@api.delete('/page/<int:pk>')
def remove_page(pk):
    return remove(Page, page_schema, pk)

@api.put('/page/<int:pk>')
def update_page(pk):
    return update(Page, page_schema, pk)

def make_nav(page):
    return {'key':page.page_id,
            'title':page.title,
            'stub':page.stub,
            'children':[make_nav(i) for i in page.children]}

def get_nav_dict(root_node):
    return make_nav(root_node)
    # if campaign.children:
    #     output = []
    #     for child in sorted(campaign.children, key=lambda x: x.order):
    #         d = {'name':child.title, 
    #                 'id':child.stub}
    #         if len(child.children) == 0:
    #             d['children'] = []
    #         elif len(child.children) > 0 and depth==0:
    #             d['load_on_demand'] = True
    #         elif len(child.children) > 0 and depth != 0:
    #             d['children'] = child.get_nav_dict(depth=depth-1)
    #             d['load_on_demand'] = True
    #         output.append(d)
    #     return output
    # return []

def as_tree(page, return_children=True):
    tree = {
        'key': page.page_id,
        'title': page.title,
        #'has_children': page.has_children,
        'num_children': len(page.children),
        'get_children': url_for('api.get_page_tree', pk=page.page_id),
        'parent': url_for('api.get_page_tree', pk=page.parent_id) if page.parent_id else None
    }
    if return_children:
        tree['children'] = [as_tree(i, False) for i in page.children]
    else:
        tree['children'] = None
    return tree

@api.get('/page/<int:pk>/tree')
def get_page_tree(pk):
    page = Page.query.get(pk)
    if not page:
        return build_response("Page not found", 404)
    return as_tree(page)

@api.put('/page/<int:pk>/tag')
def tag_page(pk, tagpk, add_or_remove):
    try:
        page = Page.get(pk)
        data = request.get_json()
        tagpk = data.tag_id
        add_or_remove = data.add_or_remove
        tag = Tag.get(tagpk)
        if add_or_remove == "add":
            if tag not in page.tags:
                page.tags.append(tag)
        elif add_or_remove == "remove":
            if tag in page.tags:
                page.tags.remove(tag)
                return build_response('success')
        else:
            return build_response('invalid verb', 400)
    except Exception as e:
        return build_response(f'invalid request {str(e)}', 400)

@api.get('/tag')
def get_tags():
    return get_all(Tag, tags_schema, 'get_tags')

@api.get('/tag/<int:pk>')
def get_tag(pk):
    return get_one(Tag, tag_schema, pk)

@api.get('/paragraph/<int:pk>')
def get_paragraph(pk):
    return get_one(Paragraph, paragraph_schema, pk)

@api.put('/paragraph/<int:pk>')
def update_paragraph(pk):
    return update(Paragraph, paragraph_schema, pk)


# ## Campaign endpoint
# @api.route('/campaign', methods=['GET'])
# def get_campaigns():
#     return campaigns_schema.dump(Campaign.query.all())

@api.get('/campaign/<int:pk>')
def get_campaign(pk):
    return get_one(Campaign, campaign_schema, pk)


 
def endpoint_factory():
    def get_all(schema, object):
        def f():
            return schema.dump(object.query.all())
        f.__name__ = 'get_' + object.__name__.lower() + 's'
        # print("running " + f.__name__)
        return f

    def get_one(schema, object):
        def f(pk):
            return schema.dump(object.query.get(pk))
        f.__name__ = 'get_' + object.__name__.lower()
        return f

    def create(schema, object):
        def f():
            try:
                data = request.get_json()
                o = object(**schema.load(data=data))
                db.session.add(o)
                db.session.commit()
                return {'message':f'New object created'}
            except Exception as e:
                return {'message':str(e)}, 500
        f.__name__ = 'make_' + object.__name__.lower()
        return f

    def remove(schema, object):
        def f(pk):
            try:
                o = object.query.get(pk)
                db.session.delete(o)
                db.session.commit()
                return {'message': 'Deleted successfully'}
            except Exception as e:
                return {'message':str(e)}, 500
        f.__name__ = 'remove_' + object.__name__.lower()
        return f 

    def update(schema, object):
        def f(pk):
            try:
                data = request.get_json()
                o = object.query.get(pk)
                for key, val in schema.load(data=data).items():
                    setattr(o, key, val)
                db.session.add(o)
                db.session.commit()
                return {'message':'Object updated'}
            except Exception as e:
                return {'message':str(e)}, 500
        f.__name__ = 'update_' + object.__name__.lower()
        return f

    # This works but doesn't allow endpoints to be decorated. 
    # It's probably too much work, tbh
    def create_endpoints(uri,obj,single_schema, many_schema):
        api.route(f'/{uri}/<int:pk>', methods=['GET'])(get_one(single_schema, obj))
        # get 1 f'/{uri}/<int:pk>' GET
        api.route(f'/{uri}', methods=['GET'])(get_all(many_schema, obj))
        # get many f'/{uri}' GET
        api.route(f'/{uri}', methods=['POST'])(create(single_schema, obj))
        # create 1 f'/{uri}' POST
        api.route(f'/{uri}/<int:pk>', methods=['PUT'])(update(single_schema, obj))
        # update 1 f'/{uri}/<int:pk>' PUT
        api.route(f'/{uri}/<int:pk>', methods=['DELETE'])(remove(single_schema, obj))
        # delete 1 f'/{uri}/<int:pk>' DELETE

    create_endpoints('/user',User,user_schema,users_schema)
    create_endpoints('/page',Page,page_schema,pages_schema)
    create_endpoints('/paragraph',Paragraph,paragraph_schema,paragraphs_schema)
    create_endpoints('/alias',Alias,alias_schema,aliases_schema)
    create_endpoints('/campaign',Campaign,campaign_schema, campaigns_schema)
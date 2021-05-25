# from .user import User
from .schema import *

userlist = ["Alice Adams","Bill Bailey","Carol Christianson","Dennis Dockers","Erin Edwards","Frank Ferruccio"]
user_dict = [{"username": username, "email":f"{username.replace(' ','').lower()}@test.com"} for username in userlist]

U = [User(**user) for user in user_dict]
for u in U:
    u.set_password("verysafe")

C = []
for i, user in enumerate(U):
    c = Campaign(f"Campaign {i}", f"campaign{i}", user)
    C.append(c)

P = []
for c in C:
    for i in range(100):
        p = Page(title=f"Test Page {i}", stub=f"testpage{i}", campaign=c)
        P.append(p)
PP=[]
for p in P:
    for sec in range(10):
        pp = Paragraph(page=p, edited_by=p.campaign.owner)
        PP.append(pp)

def maker():
    yield U
    yield C
    yield P
    yield PP

# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session

# engine = create_engine('sqlite:///e:/dev/web/lore/lore/app.db')
# with Session(engine) as session:
#     session.add_all(U)
#     session.add_all(C)
#     session.add_all(P)
#     session.add_all(PP)
#     session.commit()

# print("Rows added successfully")
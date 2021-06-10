import axios from 'axios';
// import Tree from 'rc-tree';
import Tree, { useTreeState, treeHandlers } from 'react-hyper-tree';
import { useEffect, useState } from 'react';
import useFetch from './useFetch';

const base = window.location.protocol + '//' + window.location.host + '/';

const PageTree = () => {
    const { required, instance, handlers } = useTreeState( {
        id: 'page-tree',
        data: {
            
        }
    });
    const getChildren = ({node}) => {
        console.log(node);
        console.log(base+'page/' + node.id + '/tree');
        return axios.get(base+'page/' + node.id + '/tree').then(
            result => {
                if (result.data['num_children'] == 0) {
                    console.log("isleaf");
                    node.isLeaf=true;
                }
                console.log(result);
            }
        ) ;
    };
    return (
        <Tree
            {...required}
            {...handlers}
            horizontalLineStyles={{
                stroke: '#c4c4c4',
                strokeWidth: 1,
                strokeDasharray: '1 4',
            }}
            verticalLineStyles={{
                stroke: '#c4c4c4',
                strokeWidth: 1,
                strokeDasharray: '1 4',
            }}
            draggable={false}
            gapMode={'padding'}
            depthGap={30}
            disableLines={false}
            disableHorizontalLines={false}
            disableVerticalLines={false}
            verticalLineTopOffset={0}
            verticalLineOffset={11}
            renderNode={null}
            />
    );
//     const [ data, setData ] = useState();
//     const [ expandedKeys, setExpandedKeys ] = useState([]);
//     const [ autoExpandParent, setAutoExpandParent ] = useState(true);

// useEffect(() => {
//     setData([
//    {"title":"0-0-label",
//     "key":"0-0-key",
//     "children":[{"title":"0-0-0-label",
//                  "key":"0-0-0-key",
//                  "children":[{"title":"0-0-0-0-label",
//                               "key":"0-0-0-0-key"},
//                              {"title":"0-0-0-1-label",
//                               "key":"0-0-0-1-key"},
//                              {"title":"0-0-0-2-label",
//                               "key":"0-0-0-2-key"}]},
//                 {"title":"0-0-1-label",
//                  "key":"0-0-1-key",
//                  "children":[{"title":"0-0-1-0-label",
//                               "key":"0-0-1-0-key"},
//                              {"title":"0-0-1-1-label",
//                               "key":"0-0-1-1-key"},
//                              {"title":"0-0-1-2-label",
//                               "key":"0-0-1-2-key"}]},
//                 {"title":"0-0-2-label","key":"0-0-2-key"}]},
//                 {"title":"0-1-label",
//                  "key":"0-1-key",
//                  "children":[{"title":"0-2-label",
//                               "key":"0-2-key"},
//                              {"title":"0-1-0-label",
//                               "key":"0-1-0-key",
//                               "children":[{"title":"0-1-0-0-label",
//                                            "key":"0-1-0-0-key"},
//                                           {"title":"0-1-0-1-label",
//                                            "key":"0-1-0-1-key"},
//                                           {"title":"0-1-0-2-label",
//                                            "key":"0-1-0-2-key"}]},
//                              {"title":"0-1-1-label",
//                               "key":"0-1-1-key",
//                               "children":[{"title":"0-1-1-0-label",
//                                            "key":"0-1-1-0-key"},
//                                            {"title":"0-1-1-1-label",
//                                             "key":"0-1-1-1-key"},
//                                            {"title":"0-1-1-2-label",
//                                             "key":"0-1-1-2-key"}]},
//                              {"title":"0-1-2-label",
//                               "key":"0-1-2-key"}]}] );
// }, []);

    
//     // state = {
//     //     gData,
//     //     autoExpandParent: true,
//     //     expandedKeys: ['0-0-key', '0-0-0-key', '0-0-0-0-key'],
//     // };
    
//     const onDragStart = info => {
//         console.log('start ', info);
//     };

//     const onDragEnter = e => {
//         console.log('enters ', e);
//     };

//     const onDrop = info => {
//         console.log('drop', info);
//         const dropKey = info.node.key;
//         const dragKey = info.dragNode.key;
//         const dropPos = info.node.pos.split('-');
//         const dropPosition = info.dropPosition - Number(dropPos[dropPos.length - 1]);

//         const loop = (data, key, callback) => {
//             data.forEach((item, index, arr) => {
//             if (item.key === key) {
//                 callback(item, index, arr);
//                 return;
//             }
//             if (item.children) {
//                 loop(item.children, key, callback);
//             }
//             });
//         };
//         // const data = [...this.state.gData];

//         // Find dragObject
//         let dragObj;
//         loop(data, dragKey, (item, index, arr) => {
//             arr.splice(index, 1);
//             dragObj = item;
//         });

//         if (dropPosition === 0) {
//             // Drop on the content
//             loop(data, dropKey, item => {
//                 // eslint-disable-next-line no-param-reassign
//                 item.children = item.children || [];
//                 // where to insert 示例添加到尾部，可以是随意位置
//                 item.children.unshift(dragObj);
//             });
//         } else {
//             // Drop on the gap (insert before or insert after)
//             let ar;
//             let i;
//             loop(data, dropKey, (item, index, arr) => {
//                 ar = arr;
//                 i = index;
//             });
//             if (dropPosition === -1) {
//                 ar.splice(i, 0, dragObj);
//             } else {
//                 ar.splice(i + 1, 0, dragObj);
//             }
//         }
//         setData(data);
//     };

//     const onExpand = _expandedKeys => {
//         console.log('onExpand', _expandedKeys);
//         setExpandedKeys(_expandedKeys);
//         setAutoExpandParent(false);
//     };

//     const fetchTree = (node) => {
//         console.log(node);
//         console.log(base+'page/' + node.id + '/tree');
//         return axios.get(base+'page/' + node.id + '/tree').then(
//             result => {
//                 if (result.data['num_children'] == 0) {
//                     console.log("isleaf");
//                     node.isLeaf=true;
//                 }
//                 console.log(result);
//             }
//         ) ;
//     }

//     return (
//         <div className="draggable-demo">
//           <h2>draggable</h2>
//           <p>drag a node into another node</p>
//           <div className="draggable-container">
//             <Tree
//               expandedKeys={expandedKeys}
//               onExpand={onExpand}
//               autoExpandParent={autoExpandParent}
//               draggable
//               onDragStart={onDragStart}
//               onDragEnter={onDragEnter}
//               onDrop={onDrop}
//               loadData={fetchTree}
//               treeData={[{'title':'root','id':1}]}
//             //   treeData={data}
//             />
//           </div>
//         </div>
//       );
}
export default PageTree;
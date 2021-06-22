import {BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { useState, createContext } from 'react';
import Navbar from './Navbar';
import Home from './Home';
import Create from './Create';
import PageDetails from './PageDetails';
import NotFound from './NotFound';
import Login from './Login'
import PageEditor from './PageEditor';
import PageTree from './PageTree';
import { IconContext } from 'react-icons/lib';
import QuillComponent from './QuillComponent';

export const UserContext = createContext();
export const CampaignContext = createContext();

function App() {
  const [ user, setUser ] = useState(null);
  const [ campaign, setCampaign ] = useState(null);

  const currentUser = {
    user: user,
    loginUser: (_user) => {setUser(_user)},
    logoutUser: () => {setUser(null)}
  }

  const currentCampaign = {
    campaign: campaign,
    useCampaign: (_campaign) => {setCampaign(_campaign) }
  }

  return (
    <UserContext.Provider value={currentUser}>
      <CampaignContext.Provider value={currentCampaign}>
        <Router>
          <div id="main" className="App">
            <IconContext.Provider value={{ className: 'react-icons', size:'2rem' }}>
              <div id="nav">
                <Navbar />
              </div>
            </IconContext.Provider>
            <div id="tree">
            <PageTree />
            </div>
              <div id="content" className="content">
              <main>
                <Switch>
                  <Route exact path="/" component={Home} />
                  <Route exact path="/create" component={Create} />
                  <Route exact path="/Test/:id" component={PageEditor} />
                  <Route exact path="/login" component={Login} />
                  <Route path="/page/:id" component={PageDetails} />
                  <Route path="/pedit/:id" component={QuillComponent } />
                  <Route path="*" component={NotFound} />
                </Switch>
                </main>
              </div>
          </div>
        </Router>
      </CampaignContext.Provider>
    </UserContext.Provider>
  );
}

export default App;
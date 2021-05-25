import {BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { useState, createContext } from 'react';
import Navbar from './Navbar';
import Home from './Home';
import Create from './Create';
import BlogDetails from './BlogDetails';
import NotFound from './NotFound';
import Login from './Login'

export const UserContext = createContext();
export const CampaignContext = createContext();

function App() {
  const [ username, setUsername ] = useState(null);
  const [ campaign_id, setCampaign ] = useState(null);

  const currentUser = {
    username: username,
    loginUser: (_username) => {setUsername(_username)},
    logoutUser: () => {setUsername(null)}
  }

  const currentCampaign = {
    campaign_id: campaign_id,
    useCampaign: (_campaign_id) => {setCampaign(_campaign_id) }
  }

  return (
    <UserContext.Provider value={currentUser}>
      <CampaignContext.Provider value={currentCampaign}>
        <Router>
          <div className="App">
            <Navbar />
            <div className="content">
              <Switch>
                <Route exact path="/" component={Home} />
                <Route exact path="/create" component={Create} />
                <Route exact path="/login" component={Login} />
                <Route path="/blogs/:id" component={BlogDetails} />
                <Route path="*" component={NotFound} />
              </Switch>
            </div>
          </div>
        </Router>
      </CampaignContext.Provider>
    </UserContext.Provider>
  );
}

export default App;
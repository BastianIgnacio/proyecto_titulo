import React, { Suspense } from 'react';
import { Redirect, Route, Switch } from 'react-router-dom';

const DataListPages = React.lazy(() =>
  import(/* webpackChunkName: "start" */ './administradoresLocalesComerciales')
);
const Gogo = ({ match }) => (
  <Suspense fallback={<div className="loading" />}>
    <Switch>
      <Redirect exact from={`${match.url}/`} to={`${match.url}/administradoresLocalesComerciales`} />
      <Route
        path={`${match.url}/administradores`}

        render={(props) => <DataListPages {...props} />}
      />
      <Redirect to="/error" />
    </Switch>
  </Suspense>
);
export default Gogo;

import React, { Suspense } from 'react';
import { Redirect, Route, Switch } from 'react-router-dom';

const LocalesComerciales = React.lazy(() =>
  import(/* webpackChunkName: "start" */ './localesComerciales')
);
const Gogo = ({ match }) => (
  <Suspense fallback={<div className="loading" />}>
    <Switch>
      <Redirect exact from={`${match.url}/`} to={`${match.url}/localesComerciales`} />
      <Route
        path={`${match.url}/locales`}

        render={(props) => <LocalesComerciales {...props} />}
      />
      <Redirect to="/error" />
    </Switch>
  </Suspense>
);
export default Gogo;

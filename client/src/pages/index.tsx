import Home from './Home'
import Details from './Details'

import { useRoutes } from 'react-router-dom';

const Index = () => {

    const routes = useRoutes([
        {
            path: "/",
            element: <Home />
        },
        {
            path: "/details/:book_id",
            element: <Details />
        },
    ]);
    return routes
}

export default Index
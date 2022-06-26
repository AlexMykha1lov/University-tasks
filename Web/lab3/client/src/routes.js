import Lists from './pages/listsPage';
import List from './pages/ListPage';

export const publicRoutes = [
    {
        path: '/',
        Component: Lists
    },

    {
        path: '/list/:id',
        Component: List
    }
]
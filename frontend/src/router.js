import Vue from 'vue'
import Router from 'vue-router'
import Test from './components/HelloWorld'
import Index from './views/index'
import TEST1 from './components/Test1'
import NotFound from './views/NotFound'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
        path: '/test',
        name: 'test',
        component: Test
    },
    {
        path: '/',
        name: 'index',
        component: Index
    },
    {
        path: '/test1',
        name: 'test1',
        component: TEST1
    },
    {
        path: '/*',
        name: 'notfound',
        component: NotFound
    }
    ]
})
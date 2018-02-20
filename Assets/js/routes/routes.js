import DashboardLayout from '../components/Dashboard/Layout/DashboardLayout.vue'

// GeneralViews
import NotFound from '../components/GeneralViews/NotFoundPage.vue'

// Dashboard Pages
import Overview from '../components/Dashboard/Views/Overview.vue'
import UserProfile from '../components/Dashboard/Views/UserProfile.vue'
import Enrollment from '../components/Dashboard/Views/Enrollment.vue'

const routes = [
  {
    path: '/',
    component: DashboardLayout,
    redirect: '/dashboard/overview'
  },
  {
    path: '/dashboard',
    component: DashboardLayout,
    redirect: '/dashboard/overview',
    children: [
      {
        path: 'overview',
        name: 'Overview',
        component: Overview
      },
      {
        path: 'enrollment',
        name: 'Enrollment',
        component: Enrollment
      },
      {
        path: 'user',
        name: 'User',
        component: UserProfile
      }
    ]
  },
  { path: '*', component: NotFound }
]

export default routes

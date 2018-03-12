import UIComponents from './UIComponents'
import TopNavbar from './Dashboard/Layout/TopNavbar.vue'
import ContentFooter from './Dashboard/Layout/ContentFooter.vue'
import DashboardContent from './Dashboard/Layout/Content.vue'
import DashboardLayout from './Dashboard/Layout/DashboardLayout.vue'
import MobileMenu from './Dashboard/Layout/MobileMenu.vue'
import UserCard from './Dashboard/Views/UserProfile/UserCard.vue'
import Overview from './Dashboard/Views/Overview.vue'
import Enrollment from './Dashboard/Views/Enrollment.vue'
import Individual from './Dashboard/Views/Enrollment/Individual.vue'

const components = {
  // Dashboard Layout
  TopNavbar,
  ContentFooter,
  DashboardContent,
  DashboardLayout,
  MobileMenu,
  // Dashboard Views
  Overview,
  Enrollment,
  //
  // UserProfile
  UserCard,
  // Enrollment
  Individual,
  // UI Components
  ...UIComponents
}

export default components

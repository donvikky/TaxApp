import UIComponents from './UIComponents'
import NotFound from './GeneralViews/NotFoundPage.vue'
import TopNavbar from './Dashboard/Layout/TopNavbar.vue'
import ContentFooter from './Dashboard/Layout/ContentFooter.vue'
import DashboardContent from './Dashboard/Layout/Content.vue'
import DashboardLayout from './Dashboard/Layout/DashboardLayout.vue'
import MobileMenu from './Dashboard/Layout/MobileMenu.vue'
import EditProfileForm from './Dashboard/Views/UserProfile/EditProfileForm.vue'
import UserCard from './Dashboard/Views/UserProfile/UserCard.vue'
import UserProfile from './Dashboard/Views/UserProfile.vue'
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
  UserProfile,
  Enrollment,
  //
  // UserProfile
  EditProfileForm,
  UserCard,
  // Enrollment
  Individual,
  // GeneralViews
  NotFound,
  // UI Components
  ...UIComponents
}

export default components

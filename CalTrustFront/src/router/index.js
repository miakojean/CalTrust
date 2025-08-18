import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue'),
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    
    {
      path:'/entreprises',
      name: 'entreprise',
      component: () => import('../views/firms.vue')
    },

    {
      path: '/entreprises/categorie/:categoryCode',
      name: 'entreprise-category',
      component: () => import('../views/FirmsCategory.vue'),
      props: true
    },

    {
      path: '/entreprises/details/:firm',
      name: 'entreprises-detail',
      component: () => import('../views-companies/details/companyDetails.vue'),
      props: true // permet d’injecter le paramètre comme prop
    },

    {
      path:'/avis',
      name: 'avis',
      component: () => import('../views/Reviews.vue')
    },
    
    /* About authentication */

    {
      path:'/signin',
      name: 'connexion',
      component: () => import('../views-authentication/login.vue')
    },
    {
      path:"/registration",
      name:"registration",
      component: () => import('../views-authentication/registration.vue')
    },
    {
      path:'/registration/firms',
      name: 'registrationFirms',
      component: () => import('@/views-authentication/composant/firms.vue')
    },
    {
      path:'/registration/consumer',
      name: 'registrationCustomer',
      component: () => import('@/views-authentication/composant/customer.vue')
    },
    {
      path:'/password-reseting',
      name:"password-reseting",
      component: () => import('@/views-authentication/composant/passworReset.vue')
    },

    // About the firm and customer profile settings screens
    {
      path:'/profilecustomer',
      name:"profilecustomer",
      component: () => import('@/profil/profilCustomer.vue')
    },
    {
      path:'/profilecustomer/security',
      name:"profilecustomer-security",
      component: () => import('@/profil/FirmView/profileSecurity.vue')
    },
    {
      path:'/profilecustomer/notifications',
      name:"profilecustomer-notifications",
      component: () => import('@/profil/FirmView/profileNotifications.vue')
    },
    {
      path:'/profilecustomer/reviews',
      name:"profilecustomer-reviews",
      component: () => import('@/profil/FirmView/profileMyReviews.vue')
    },
    {
      path:'/profilecustomer/plan',
      name:"profilecustomer-plan",
      component: () => import('@/profil/FirmView/profilePlan.vue')
    },
    
  ]
  })

export default router
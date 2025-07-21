# Authentication
└── Views-Authentication 
    ├── authtools
    |  ├── Ajout manuel/CSV  
    │  └── Catégorisation IA
    ├── composant
    |  ├── customerForm.vue
    │  └── firms.vue   
    ├── login.vue
    ├── loginSection.vue
    ├── regisForm.vue
    ├── registration.vue
    ├── registrationSection.vue   

How authentication must work? 

Firstly, there are two choices:
-I'm a customer
-I'm a firm
Once choice is done, we go on another url() which can be an
``` js
  {
    path:'/registration/firms',
    name: 'registrationFirms',
    component: () => import('@/views-authentication/composant/firms.vue')
  }, /* the firm route's  */
  {
    path:'/registration/consumer',
    name: 'registrationCustomer',
    component: () => import('@/views-authentication/composant/customerform.vue')
  }, /* the consumer route's  */

```

Our JSON file expected for firm and simple_user:
``` json
{
  "username": "new_firm",
  "email": "firm@business.com",
  "password": "supersecurepassword",
  "user_type": "firm",
  "company_name": "Tech Solutions Inc.",
  "company_category": "Commerce",
  "siret": "12345678901234",
  "address": "123 Tech Park, Innovation City"
}
```

``` json
{
  "username": "new_customer_user",
  "email": "customer@example.com",
  "password": "securepassword123",
  "user_type": "customer",
  "phone": "0123456789",
  "birth_date": "1990-05-20"
}
```

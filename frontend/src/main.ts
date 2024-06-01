import { createApp } from 'vue';
import App from './App.vue';
import PrimeVue from 'primevue/config';

import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import Dialog from 'primevue/dialog';


import 'primevue/resources/themes/aura-light-green/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';

const app = createApp(App);

app.use(PrimeVue);

app.component('VueButton', Button);
app.component('VueInputText', InputText);
app.component('VueDialog', Dialog);

app.mount('#app');

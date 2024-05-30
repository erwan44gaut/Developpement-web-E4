import { createApp } from 'vue';
import App from './App.vue';
import PrimeVue from 'primevue/config';
import FloatLabel from 'primevue/floatlabel';
import Button from 'primevue/button';
import Card from 'primevue/card';


import 'primevue/resources/themes/aura-light-green/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';

const app = createApp(App);

app.use(PrimeVue);

app.component('VueFloatLabel', FloatLabel);
app.component('VueButton', Button);
app.component('VueCard', Card);

app.mount('#app');

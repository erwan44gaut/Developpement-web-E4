import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import PrimeVue from 'primevue/config';
import './assets/main.css';
import './assets/base.css';

import Button from 'primevue/button';
import Checkbox from 'primevue/checkbox';
import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import RadioButton from 'primevue/radiobutton';
import SelectButton from 'primevue/selectbutton';
import TabPanel from 'primevue/tabpanel';
import TabView from 'primevue/tabview';

import 'primeicons/primeicons.css';
import 'primevue/resources/primevue.min.css';
import 'primevue/resources/themes/aura-light-green/theme.css';

const app = createApp(App);

app.use(PrimeVue);
app.use(router);

app.component('VueButton', Button);
app.component('VueInputText', InputText);
app.component('VueDialog', Dialog);
app.component('VueRadioButton', RadioButton);
app.component('VueTabView', TabView);
app.component('VueTabPanel', TabPanel);
app.component('VueCheckbox', Checkbox);
app.component('VueSelectButton', SelectButton);

app.mount('#app');

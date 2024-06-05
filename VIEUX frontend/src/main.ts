import { createApp } from 'vue';
import App from './App.vue';
import PrimeVue from 'primevue/config';
import './global.css';


import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import Dialog from 'primevue/dialog';
import RadioButton from 'primevue/radiobutton';
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
import Checkbox from 'primevue/checkbox';
import SelectButton from 'primevue/selectbutton';

import 'primevue/resources/themes/aura-light-green/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';

const app = createApp(App);

app.use(PrimeVue);

app.component('VueButton', Button);
app.component('VueInputText', InputText);
app.component('VueDialog', Dialog);
app.component('VueRadioButton', RadioButton);
app.component('VueTabView', TabView);
app.component('VueTabPanel', TabPanel);
app.component('VueCheckbox', Checkbox);
app.component('VueSelectButton', SelectButton);

app.mount('#app');

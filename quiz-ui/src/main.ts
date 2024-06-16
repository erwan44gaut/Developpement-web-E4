import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import PrimeVue from 'primevue/config';
import ConfirmationService from 'primevue/confirmationservice';
import ToastService from 'primevue/toastservice';
import './assets/main.css';
import './assets/base.css';

import Button from 'primevue/button';
import Checkbox from 'primevue/checkbox';
import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import RadioButton from 'primevue/radiobutton';
import SelectButton from 'primevue/selectbutton';
import TabView from 'primevue/tabview';
import Password from 'primevue/password';
import Image from 'primevue/image';
import Chart from 'primevue/chart';
import ScrollPanel from 'primevue/scrollpanel';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ConfirmDialog from 'primevue/confirmdialog';
import Card from 'primevue/card';

import 'primeicons/primeicons.css';
import 'primevue/resources/primevue.min.css';
import 'primevue/resources/themes/aura-light-green/theme.css';

const app = createApp(App);

app.use(PrimeVue);
app.use(ConfirmationService);
app.use(ToastService);
app.use(router);

app.component('VueButton', Button);
app.component('VueInputText', InputText);
app.component('VueDialog', Dialog);
app.component('VueRadioButton', RadioButton);
app.component('VueTabView', TabView);
app.component('VueCheckbox', Checkbox);
app.component('VueSelectButton', SelectButton);
app.component('VuePassword', Password);
app.component('VueImage', Image);
app.component('VueScrollPanel', ScrollPanel);
app.component('VueDataTable', DataTable);
app.component('VueColumn', Column);
app.component('VueChart', Chart);
app.component('VueConfirmDialog', ConfirmDialog);
app.component('VueCard', Card);

app.mount('#app');

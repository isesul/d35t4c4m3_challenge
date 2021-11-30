import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";

import AdminBuses from "../views/admin/Buses.vue";
import BusDrivers from "../views/admin/BusDrivers.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },

  {
    path: "/buses",
    name: "AdminBuses",
    component: AdminBuses,
  },
  {
    path: "/drivers",
    name: "BusDrivers",
    component: BusDrivers,
  },
];

const router = new VueRouter({
  mode: "hash",
  base: process.env.BASE_URL,
  routes,
});

export default router;

<template>
  <v-app id=" app">
    <v-navigation-drawer
      v-model="drawer"
      color="menu"
      :clipped="$vuetify.breakpoint.lgAndUp"
      app
      width="350"
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6"> D3t4c4m3 </v-list-item-title>
          <v-list-item-subtitle> Challenge </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense nav>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.path"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-slide-y-transition mode="out-in">
        <router-view />
      </v-slide-y-transition>
    </v-main>

    <v-footer dark padless app :clipped-left="$vuetify.breakpoint.lgAndUp">
      <v-card color="primary" class="flex" flat tile>
        <v-card-text class="py-2 white--text text-center">
          Benjamin Segura {{ new Date().getFullYear() }}
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      drawer: true,
      right: null,

      items: [
        {
          nombre: "Buses",
          path: "buses",
          title: "Administrar Buses",
          icon: "directions_bus",
        },
        {
          nombre: "drivers",
          path: "drivers",
          title: "Administrar conductores",
          icon: "engineering",
        },
        {
          nombre: "Passenger",
          path: "passenger",
          title: "Administrar Passenger",
          icon: "people",
        },
        {
          nombre: "Travels",
          path: "viajes",
          title: "Administrar viajes",
          icon: "people",
        },
      ],
    };
  },
  computed: {},
  created() {},
  methods: {},
};
</script>

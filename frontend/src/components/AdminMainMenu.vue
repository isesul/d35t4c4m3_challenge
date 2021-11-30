<template>
  <nav>
    <v-toolbar app>
      <v-toolbar-side-icon @click="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title class="headline text-uppercase">
        <router-link :to="{ name: 'home' }">
          <span>Vue</span>
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn>
        <span class="mr-2">Cerrar sesión</span>
        <v-icon>fas fa-address-book</v-icon>
      </v-btn>
    </v-toolbar>

    <v-navigation-drawer v-model="drawer" class="indigo" app>
      <v-layout column align-center mt-5>
        <v-flex>
          <v-avatar> </v-avatar>
        </v-flex>
        <v-flex>
          <p class="mt-3 white--text">test</p>
        </v-flex>
      </v-layout>

      <v-divider></v-divider>

      <v-list>
        <v-list-tile v-for="(item, index) in items" :key="index" :to="item.to">
          <v-list-tile-action>
            <v-icon class="white--text">{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title class="white--text">{{
              item.title
            }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      items: [
        {
          nombre: "Buses",
          path: "/buses",
          to: { name: "buses" },
          title: "Administrar Buses",
          icon: "directions_bus",
        },
        {
          nombre: "Conductores",
          to: { name: "conductores" },
          path: "/conductores",
          title: "Administrar Conductores",
          icon: "engineering",
        },
        {
          nombre: "Passenger",
          to: { name: "passenger" },
          path: "/passenger",
          title: "Administrar Passenger",
          icon: "people",
        },
        {
          nombre: "Travels",
          to: { name: "travels" },
          path: "/travels",
          title: "Administrar Viajes",
          icon: "departure_board",
        },
      ],
    };
  },
  computed: {},
  methods: {},
};
</script>

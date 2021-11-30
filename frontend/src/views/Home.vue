<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="10" md="10">
        <v-text-field
          v-model="search"
          label="Buscador"
          placeholder="Escriba lo que desea buscar en youtube"
          solo
          @keyup.enter.native="buscar"
        ></v-text-field>
        <span v-show="error" style="color: red"
          >Tiene que escribir algun valor para buscar</span
        >
      </v-col>
      <v-col cols="12" sm="2" md="2">
        <v-btn
          color="primary"
          style="height: 50px; min-width: 120px"
          @click="buscar"
        >
          Buscar
        </v-btn>
      </v-col>
    </v-row>

    <v-row dense>
      <v-col v-for="(item, i) in items" :key="i" cols="12">
        <v-card color="white">
          <div class="d-flex flex-no-wrap">
            <v-img class="ma-3" max-width="300" tile>
              <v-img :src="item.image"></v-img>
            </v-img>
            <div>
              <v-card-title class="headline" v-text="item.title"></v-card-title>

              <v-card-subtitle v-text="item.description"></v-card-subtitle>
              <v-card-actions>
                <v-btn
                  text
                  :href="'https://youtube.com/watch?v=' + item.videoId"
                  target="_blank"
                >
                  ver video
                </v-btn>
              </v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      search: "",
      items: [],
      error: false,
    };
  },
  methods: {
    async buscar() {
      let me = this;
      if (me.search.length == 0) {
        me.error = true;
      } else {
        me.error = false;
        const data = {
          search: me.search,
        };
        const res = await fetch(
          "https://youtube-search-jc.herokuapp.com/api/youtube/search",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
          }
        );
        const results = await res.json();
        me.items = results.data;
      }
    },
  },
};
</script>

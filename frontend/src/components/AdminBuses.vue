<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    sort-by="id"
    class="elevation-1"
  >
    <template #top>
      <v-toolbar flat>
        <v-toolbar-title>Buses</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <template #activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
              Agregar
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.name"
                      label="Name"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.patent"
                      label="Patent"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close"> Cancel </v-btn>
              <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5"
              >Are you sure you want to delete this item?</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete"
                >Cancel</v-btn
              >
              <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                >OK</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template #item.actions="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
      <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
    </template>
    <template #no-data>
      <v-btn color="primary" @click="initialize"> Reset </v-btn>
    </template>
  </v-data-table>
</template>

<script>
import axios from "axios";
import { DateTime } from "luxon";

export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,
    headers: [
      { text: "#", value: "id" },
      { text: "name", value: "name" },
      { text: "patent", value: "patent" },
      { text: "created", value: "created_at" },
      { text: "modify", value: "modify_at" },
      { text: "actions", value: "actions" },
    ],
    desserts: [],
    editedIndex: -1,
    editedItem: {
      name: "",
      patent: "",
    },
    defaultItem: {
      name: "",
      patent: "",
    },
    currentItem: null,
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Agregar" : "Edit Item";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    initialize() {
      axios.get("/api/function_views/bus/").then((response) => {
        this.desserts = response.data;
        this.desserts.forEach((data) => {
          data.modify_at = DateTime.fromISO(data.modify_at)
            .setLocale("cl")
            .toFormat("ff");
          data.created_at = DateTime.fromISO(data.created_at)
            .setLocale("cl")
            .toFormat("ff");

          console.log(data);
        });

        console.log("this.desserts: ", this.desserts);
      });
    },

    editItem(item) {
      this.currentItem = item;
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
      console.log("editItem", this.editedIndex);
    },

    deleteItem(item) {
      this.currentItem = item;
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      let self = this;
      axios
        .delete(
          `/api/function_views/bus/${this.currentItem.id}/`,
          self.editedItem
        )
        .then((response) => {
          this.initialize();
          this.dialogDelete = false;
        });
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        let self = this;
        axios
          .put(
            `/api/function_views/bus/${this.currentItem.id}/`,
            self.editedItem
          )
          .then((response) => {
            this.initialize();
          });
      } else {
        let self = this;
        axios
          .post(`/api/function_views/bus/`, self.editedItem)
          .then((response) => {
            this.initialize();
          });
      }
      this.close();
    },
  },
};
</script>

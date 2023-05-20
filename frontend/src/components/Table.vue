<template>
  <div class="p-2 w-[700px] overflow-x-auto">
    <Vue3EasyDataTable
      table-class-name="customize-table"
      :headers="headers"
      :items="items"
    />
  </div>
</template>

<script>
import Vue3EasyDataTable from "vue3-easy-data-table";
import "vue3-easy-data-table/dist/style.css";
export default {
  components: {
    Vue3EasyDataTable,
  },
  data() {
    return {

      headers: [
        { text: "Адрес постамата", value: "adress", sortable: true },
        { text: "Количество отзывов", value: "review", sortable: true },
        { text: "Рейтинг", value: "rating", sortable: true },
        { text: "Категория проблемы", value: "problem", sortable: true },
      ],
      items: [
        {
          adress: "пр.корелева 62",
          review: "1000",
          rating: 9,
          problem: "Рок играет всю ночь",
        },
        {
          adress: "Stephen Curry",
          review: "GSW",
          rating: 30,
          problem: "G",
        },
        {
          adress: "Stephen Curry",
          review: "GSW",
          rating: 30,
          problem: "G",
        },
        {
          adress: "Stephen Curry",
          review: "GSW",
          rating: 30,
          problem: "G",
        },
      ],
    };
  },
  computed:{
    postamat_unique_list() {
      let adress_list = [];
      this.postamats_list.forEach((element) => adress_list.push(element.adress));
      console.log(adress_list);
      let unique_postamat_list = Array.from(new Set(adress_list));
      console.log(unique_postamat_list.length);
      return unique_postamat_list;
    },
    postamat_table_info_count(){
      table_info_count = [{
        adress: '',
        review: 0,
        rating: 0,
        problem: 1,
      }];
      this.postamat_unique_list.forEach((element) => {
        this.postamat_list.forEach((element2) => {
          if (element = element2.adress) {
            
          }

        })
})
    }
  },
  props:{
    postamats_list: Array
  }
};
</script>

<style>
.customize-table {
  --easy-table-border: 2px solid #ff1935;
  --easy-table-row-border: 1px solid #000000;

  --easy-table-header-font-size: 16px;
  --easy-table-header-height: 70px;
  --easy-table-header-font-color: #ffffff;
  --easy-table-header-background-color: #ff1935;

  --easy-table-header-item-padding: 10px 15px;

  --easy-table-body-even-row-font-color: #fff;
  --easy-table-body-even-row-background-color: #82898f;

  --easy-table-body-row-font-color: #000000;
  --easy-table-body-row-background-color: #ffffff;
  --easy-table-body-row-height: 50px;
  --easy-table-body-row-font-size: 16px;

  --easy-table-body-row-hover-font-color: #000000;
  --easy-table-body-row-hover-background-color: #f4d8d8;

  --easy-table-body-item-padding: 10px 15px;

  --easy-table-footer-background-color: #ffffff;
  --easy-table-footer-font-color: #000000;
  --easy-table-footer-font-size: 14px;
  --easy-table-footer-padding: 0px 10px;
  --easy-table-footer-height: 50px;

  --easy-table-rows-per-page-selector-width: 70px;
  --easy-table-rows-per-page-selector-option-padding: 10px;
  --easy-table-rows-per-page-selector-z-index: 1;

  --easy-table-scrollbar-track-color: #2d3a4f;
  --easy-table-scrollbar-color: #5e3636;
  --easy-table-scrollbar-thumb-color: #4c5d7a;
  --easy-table-scrollbar-corner-color: #2d3a4f;

  --easy-table-loading-mask-background-color: #4f2d2d;
}
</style>

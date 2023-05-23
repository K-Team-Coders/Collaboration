<template>
  <div class="w-full mr-3 mt-2 text-xs overflow-x-auto">
    <Vue3EasyDataTable
      table-class-name="customize-table"
      class="shadow-cards"
      style="border-radius: 6px"
      :headers="headers"
      :items="items"
      
    />
  </div>
  <div>
    
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
          adress: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum, libero. Enim fugiat possimus officia dolor quod. In officia dolor pariatur ducimus facere adipisci. Velit tempore, quos eaque aliquam debitis vero?",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },
        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },
        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },
        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },
        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },
        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },
        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },
        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },
        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },
        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },
        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },

        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },

        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },
        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
        },

        {
          adress: "г.Москва, ул. Королева, д.62",
          review: "14",
          rating: "4.9 / 5.0",
          problem: "Сломан",
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
  computed: {
    postamat_unique_list() {
      let adress_list = [];
      this.postamats_list.forEach((element) =>
        adress_list.push(element.adress)
      );
      let unique_postamat_list = Array.from(new Set(adress_list));
      return unique_postamat_list;
    },
    postamat_table_info_count() {
      let table_info_count = [];
      let adress = "";
      let review = 0;
      let rating = 0;
      let problem = 1;
      this.postamat_unique_list.forEach((element) => {
        this.postamat_list.forEach((element2) => {
          if ((element = element2.adress)) {
            review += 1;
            rating += 1;
          }
        });
        table_info_count.push({
          element,
          review,
          rating,
          problem,
        });
        review = 0;
        rating = 0;
      });

      return table_info_count;
    },
  },
  props: {
    postamats_list: Array,
  },
};
</script>

<style>
.customize-table {
  --easy-table-border: 2px solid #ff1935;
  --easy-table-row-border: 1px solid #000000;

  --easy-table-header-font-size: 19px;
  --easy-table-header-height: 70px;
  --easy-table-header-font-color: #ffffff;
  --easy-table-header-background-color: #ff1935;

  --easy-table-header-item-padding: 10px 15px;

  --easy-table-body-even-row-font-color: #fff;
  --easy-table-body-even-row-background-color: #82898f;

  --easy-table-body-row-font-color: #000000;
  --easy-table-body-row-background-color: #ffffff;
  --easy-table-body-row-height: 50px;
  --easy-table-body-row-font-size: 13px;

  --easy-table-body-row-hover-font-color: #000000;
  --easy-table-body-row-hover-background-color: #d7d7d7;

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

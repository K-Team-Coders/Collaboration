import axios from 'axios'
export default {
  state: {
    postamats_list: [
    ],
    filterdata: {
      
    }
  },
  mutations: {
    SET_ALLPOSTAMATS: (state, payload) => {
      state.postamats_list = payload;
    },
    SET_FILTER(state, filterdata) {
      state.filterdata = filterdata;
    }
  },
  getters: {
    allpostamats(state) {
      return state.postamats_list;
    },
    filter(state) {
      return state.filterdata;
    },
  },
  actions: {
    GET_ALLPOSTAMATS: async (context, payload) => {
      let postamats_list = await axios.get('http://26.200.185.61:8080/getAdminPageData/');
      context.commit("SET_ALLPOSTAMATS", postamats_list.data);
      console.log(typeof postamats_list.data.timeStats)
    },
    // SEND_FILTER_DATA: async (context,filterdata) => {
    //   await axios.post('http://26.200.185.61:8080/getAdminPageData/', filterdata).then(response => {
    //     let postamats_list = response; 
    //     context.commit("SET_ALLPOSTAMATS", postamats_list.data)});
      
    //   console.log(drone_list);
    // },
}}

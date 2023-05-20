import axios from 'axios'
export default {
  state: {
    postamats_list: [
    ],
  },
  mutations: {
    SET_ALLPOSTAMATS: (state, payload) => {
      state.postamats_list = payload;
    },
  },
  getters: {
    allpostamats(state) {
      return state.postamats_list;
    },
  },
  actions: {
    GET_ALLPOSTAMATS: async (context, payload) => {
      let postamats_list = await axios.get('http://26.200.185.61:8080/getAdminPageData/');
      context.commit("SET_ALLPOSTAMATS", postamats_list.data);
      
    },
}}

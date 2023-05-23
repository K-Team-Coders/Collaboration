<template>
  <div class="w-[275px]">
    <Bar  :chart-data="chartData" />
  </div>
</template>

<script>
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

export default {
  name: "BarChart",
  components: { Bar },
  data() {
    return {
      chartData: {
        labels: ["Игорь", "Артем", "Жора", "Захар", "Кирилл"],
        datasets: [
          {
            label: "Распределение проблем по отзывам",
            backgroundColor: "#E5102A",
            data: [40, 20, 12,0,100],
          },
        ],
      },
    };
  },
};
</script>

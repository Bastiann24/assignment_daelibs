<template>
  <div>
    <table class="table table-hover">
      <thead class="table-light">
        <tr>
          <th scope="col" class="text-start px-5">Name</th>
          <th scope="col">Target Score</th>
          <th scope="col">Actual Score</th>
          <th scope="col">Total Points</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td class="text-start px-5">{{ item.name }}</td>
          <td>{{ item.target }}%</td>
          <td>
            <span v-bind:class="getClass(item.target, item.actual)">
              {{ item.actual }}%
            </span></td>
          <td>{{ item.points }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: []
    }
  },
  mounted() {
    const data = [
      {
        "name": "Lauren Vickers",
        "target": 90,
        "actual": 95,
        "points": 69
      },
      {
        "name": "Shazia Darby",
        "target": 80,
        "actual": 88,
        "points": 26
      },
      {
        "name": "Zara Cain",
        "target": 85,
        "actual": 81,
        "points": 124
      },
      {
        "name": "Clair Newton",
        "target": 80,
        "actual": 22,
        "points": 82
      },
      {
        "name": "April Bruce Kieran",
        "target": 90,
        "actual": 92,
        "points": 26
      },
      
    ];
    this.items = data
  },
  methods: {
    getClass(target, actual) {
      if (target > actual) {
        return "rectangle-red";
      } else {
        return 'rectangle-green';
      }


    }
  }
}
</script>

<style scoped>
.table-hover {
  width: 1073px;
  height: 468px;
  margin-left: auto;
  margin-right: auto;
  justify-content: center;
  font-family:open Arial, Helvetica, sans-serif
}
.table td {
  padding: 30px;
}

.table-light {
  color: #5A5A5A;
}
.rectangle-red {
  border-radius: 5px;
  background-color: #ED5E61;
  padding: 5px;
  color: white;
}
.rectangle-green {
  border-radius: 5px;
  background-color: #59B77A;
  padding: 5px;
  color: white;
}
</style>
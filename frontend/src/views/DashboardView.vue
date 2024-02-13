<template>
    <div class="dashboard-view">
      <h1>Dashboard</h1>
      
      <div class="buttons-container">
        <button class="download-button" @click="baixarPDF">Baixar em PDF</button>
        <button class="download-button" @click="baixarExcel">Baixar em Excel</button>
      </div>
      
    <!-- Formulário de filtro -->
    <form @submit.prevent="filtrarDados" class="filter-form">
  <div class="form-group">
    <label for="filtro">Filtrar por:</label>
    <select id="filtro" v-model="tipoFiltro" @change="atualizarTipoInput" class="form-control">
      <option value="data">Data</option>
      <option value="vendedor">Vendedor</option>
      <option value="cliente">Cliente</option>
    </select>
  </div>
  <div v-if="tipoFiltro === 'data'" class="form-group">
    <label for="data">Data:</label>
    <input type="date" id="data" v-model="valorFiltro" class="form-control">
  </div>
  <div v-else-if="tipoFiltro === 'vendedor'" class="form-group">
    <label for="nomeVendedor">Nome do Vendedor:</label>
    <input type="text" id="nomeVendedor" v-model="valorFiltro" class="form-control">
  </div>
  <div v-else class="form-group">
    <label for="nomeCliente">Nome do Cliente:</label>
    <input type="text" id="nomeCliente" v-model="valorFiltro" class="form-control">
  </div>
  <button type="submit" class="submit-button">Filtrar</button>
</form>
      
      <!-- Lista de vendas filtradas -->
      <div class="sales-list" v-if="vendasFiltradas.length">
        <div class="sale-item" v-for="venda in vendasFiltradas" :key="venda.id">
          <div class="sale-details">
            <p><strong>ID:</strong> {{ venda.id }}</p>
            <p><strong>Data:</strong> {{ venda.data }}</p>
            <p><strong>Vendedor:</strong> {{ venda.vendedor_nome }}</p>
            <p><strong>Cliente:</strong> {{ venda.cliente_nome }}</p>
            <p>Valor Total: {{ venda.valor_total }}</p>
            <!-- Botao de excluir -->
            <button @click="excluirVenda(venda.id)" class="delete-button">Excluir</button>
          </div>
        </div>
      </div>
      <div class="no-results" v-else>
        <p>Nenhum resultado encontrado.</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'DashboardView',
    data() {
      return {
        nomeCliente: '',
        data: '',
        nomeVendedor: '',
        vendasFiltradas: [],
        tipoFiltro: 'data', // Adiciona o tipo de filtro e o valor inicial
      valorFiltro: '' ,
      };
    },
    methods: {

      filtrarDados() {
  if (this.tipoFiltro === 'data') {
    axios.get('http://localhost:8000/dashboard', {
      params: {
        data_inicio: this.valorFiltro,
      }
    })
    .then(response => {
      this.vendasFiltradas = response.data.vendas;
    })
    .catch(error => {
      console.error('Erro ao filtrar dados:', error);
    });
  } else {
    axios.get('http://localhost:8000/dashboard', {
      params: {
        nome_cliente: this.nomeCliente,
        nome_vendedor: this.nomeVendedor
      }
    })
    .then(response => {
      this.vendasFiltradas = response.data.vendas;
    })
    .catch(error => {
      console.error('Erro ao filtrar dados:', error);
    });
  }
},

      baixarPDF() {
  axios.get('http://localhost:8000/gerar_relatorio_pdf/', { responseType: 'blob' })
    .then(response => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'relatorio.pdf');
      document.body.appendChild(link);
      link.click();
    })
    .catch(error => {
      console.error('Erro ao baixar relatório PDF:', error);
    });
},

baixarExcel() {
  axios.get('http://localhost:8000/gerar_relatorio_excel/', { responseType: 'blob' })
    .then(response => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'relatorio.xlsx');
      document.body.appendChild(link);
      link.click();
    })
    .catch(error => {
      console.error('Erro ao baixar relatório Excel:', error);
    });
},



    excluirVenda(id) {
      if (confirm('Tem certeza que deseja excluir esta venda?')) {
        axios.delete(`http://localhost:8000/vendas/${id}`)
          .then(response => {
            // Remover a venda excluída da lista de vendas
            this.vendasFiltradas = this.vendasFiltradas.filter(venda => venda.id !== id);
            console.log('Venda excluída com sucesso.');
          })
          .catch(error => {
            console.error('Erro ao excluir venda:', error);
          });
      }
    }
  }
}
  </script>
  
  <style scoped>
.dashboard-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.buttons-container {
  margin-bottom: 20px;
}

.download-button {
  margin-right: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

.filter-form {
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 10px;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.submit-button {
  background-color: #28a745;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

.sales-list {
  border-top: 1px solid #ccc;
  margin-top: 20px;
  padding-top: 20px;
}

.sale-item {
  margin-bottom: 20px;
}

.sale-details {
  background-color: #f9f9f9;
  padding: 10px;
  border-radius: 5px;
}

.no-results {
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid #ccc;
}

.delete-button {
  background-color: #dc3545;
  color: #fff;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
}
  </style>
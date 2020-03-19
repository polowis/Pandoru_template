<template>
  
    <div class="container" id="wrapper">
         <form name="createForm" class="form" novalidate>
             <h1 class="rainbow">Welcome back, {{ user.name }}! What would you like to do today?</h1>
             <section class="row">
            <div class="col-1" id="addTask">
            <input class="form-control" type="text" v-model="title" placeholder="Give your task a title" required />
            <input class="form-control" type="text" v-model="description" placeholder="I need to..." required />
              <button class="add" @click.prevent="addItem" data-ng-disabled="createForm.$invalid">➕</button>
            </div>
             <div class="col-1" id="search">
          <input type="text" class="form-control" data-ng-model="todoSearch.name" placeholder=" Search Tasks   🔎" />
        </div>
             </section>
         <section class="row" id='actions'>
        <div class="col-1">
          <button class='control' data-ng-disabled="!doneCount()>0" @click.prevent="deleteComplete()">Delete Completed</button>
        </div>
         <div class="col-1">
          <button class='control' @click.prevent="markAllDone()" data-ng-disabled="!almostOneNotDone()">Mark All Completed</button>
        </div>
         <div class="col-1">
          <button class='control' @click.prevent="uncheckAllDone()" data-ng-disabled="!doneCount()>0">Unmark All Completed</button>
        </div>
        <div class="col-1">
          <button class='control' @click.prevent="deleteAll()" data-ng-disabled="!todos.length">Delete All</button>
        </div>
      </section>
       <section class="row" id='stats'>
        <div class="col-1">
          <span v-if="this.task.length < 1">No&nbsp;</span><span v-if="this.task.length < 1">Tasks&nbsp;</span><span v-if="this.task.length >= 1">Tasks&nbsp;<span class="badge" >Remaining&nbsp; {{this.task.length}} </span></span>
        </div>
        <div class="col-1">
          <div class="text-right">Today is {{ getDate() }}</div>
        </div>
        <div class="col-1">
          <div class="text-right">Task details</div>
        </div>
      </section>
       <section class="row">
        <div class='col-2' id='items'>
          <span class="todoName text-center" v-if="this.task.length < 1">Good Job! All Tasks Are Complete.</span>
        </div>
      </section>
       <section class="row" v-for="item in task" :key="item.id">
        <div class="col-2" id='ac'>
          <label>Done
            <br>
            <input class="form-control" v-model="item.done"  @click.prevent="markItemAsDone(item)" type="checkbox" name="done" />
          </label>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <label id='del'>Delete
            <br>
            <button type="button" @click.prevent="deleteItem(item)" name="delete"></button>
          </label>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
           <label id='pro' v-if="item.progress == 1">In Progress
            <br>
            <button type="pro" name="pro" id="progress_status"></button>
          </label>
        </div>
        <div class="col-2" id="list" >
          <span class="todoName"  :class="{toDoLineDone: item.done}" @click="showModal = true">{{ item.title }}</span>
          </div>
          <div class="col-2" id="list">
            <span class="todoname" :class="{toDoLineDone: item.done}">{{ item.description }}</span>
          </div>
          <ModalComponent :items="item" v-if="showModal" :title="item.title" :desc="item.description" @close="showModal = false">
            
      </ModalComponent>
          </section>  
          <section class = 'row' id = 'cls'>
           <div class = "col-2" >
            <button ng-click = 'clear()' >Clear My Local Storage</button>
           </div>
        </section>
         </form>
        </div>
    
</template>
<script>

import ModalComponent from './ModalComponent'

export default {
    props: ['user'],
    components: {
      ModalComponent
    },

    data() {
        return{
          title: '',
          progress: true,
          description: '',
          done: false,
          showModal: false,
          task: [{
            id: 0,
            title: 'test',
            description: 'test1',
            progress: 1,
            done: 0,
          }],
          token:document.head.querySelector('meta[name="csrf-token"]').content
        }
        
    },

    created() {
        socket.on('new user')
    },

    methods: {
      addItem() {
        
        axios.post('/api/create', {title: this.title, description: this.description, progress: this.progress}).then(response => {
          this.task.push({
            id: response.data.id,
            title: response.data.title,
            description: response.data.description,
            done: response.data.done,
            progress: response.data.progress,
          })

          this.title = ""
          this.description = ""

        }).then((res) =>{

        }).catch(error =>{
                
          });
       
      },

      fetchItemList() {
        axios.get('/api/todolist/'+ this.user.user_id).then(response => {
          this.task = response.data;
        });
      },

      deleteAll() {
        for(let item = 0; item < this.task.length; item++) {
            axios.post('/api/delete/' + this.task[item].id).then(response => {
              this.task = []
          }).then((res) =>{

          }).catch(error =>{
                  
          });
          }
      },
      deleteItem(item) {
        let item_id = this.task[this.task.indexOf(item)].id
        axios.post('/api/delete/' + item_id).then(response => {
          this.task.splice(this.task.indexOf(item), 1)
        }).then((res) =>{

        }).catch(error =>{
                
        });
        
        
      },
      markItemAsDone(item)
      {
        let item_element = this.task[this.task.indexOf(item)]
        axios.post('/api/done/' + item_element.id).then(response => {
          item_element.done = true;
          item_element.progress = false;
          
        }).then((res) =>{

        }).catch(error =>{
                
        });
      },

      getDate() {
         let today = new Date();
         let mm = today.getMonth() + 1;
          let dd = today.getDate();
          let yyyy = today.getFullYear();
          let date = mm + "/" + dd + "/" + yyyy;
          return date;
      },
      deleteComplete() {
        for(let item = 0; item < this.task.length; item++) {
            if(this.task[item].done == true || this.task[item].done == 1){
                axios.post('/api/delete/' + this.task[item].id).then(response => {
                  this.task.splice(item, 1)
              }).then((res) =>{

              }).catch(error =>{
                      
              });
                }
          }
      }

    },
    beforeMount(){
      this.fetchItemList()
    }

}
    
</script>
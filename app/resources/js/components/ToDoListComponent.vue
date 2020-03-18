<template>
  
    <div class="container" id="wrapper">
         <form name="createForm" class="form" novalidate>
             <h1 class="rainbow">Welcome back, {{ user.name }}! What would you like to do today?</h1>
             <section class="row">
            <div class="col-1" id="addTask">
            <input class="form-control" type="text" v-model="label" placeholder="Give your task a label" required />
            <input class="form-control" type="text" v-model="description" placeholder="I need to..." required />
              <button class="add" @click.prevent="addItem" data-ng-disabled="createForm.$invalid">➕</button>
            </div>
             <div class="col-1" id="search">
          <input type="text" class="form-control" data-ng-model="todoSearch.name" placeholder=" Search Tasks   🔎" />
        </div>
             </section>
         <section class="row" id='actions'>
        <div class="col-1">
          <button class='control' data-ng-disabled="!doneCount()>0" data-ng-click="clearCompleted()">Delete Completed</button>
        </div>
         <div class="col-1">
          <button class='control' @click="markAllDone()" data-ng-disabled="!almostOneNotDone()">Mark All Completed</button>
        </div>
         <div class="col-1">
          <button class='control' @click="uncheckAllDone()" data-ng-disabled="!doneCount()>0">Unmark All Completed</button>
        </div>
        <div class="col-1">
          <button class='control' @click="deleteAll()" data-ng-disabled="!todos.length">Delete All</button>
        </div>
      </section>
       <section class="row" id='stats'>
        <div class="col-1">
          <span>No&nbsp;</span>Tasks&nbsp;<span class="badge" >Remaining&nbsp; </span>
        </div>
        <div class="col-1">
          <div class="text-right">Today is</div>
        </div>
      </section>
       <section class="row">
        <div class='col-2' id='items'>
          <span class="todoName text-center" v-if="this.task.length < 1">Good Job! All Tasks Are Complete.</span>
        </div>
      </section>
       <section class="row" v-for="item in task" :key="item.label">
        <div class="col-2" id='ac'>
          <label>Done
            <br>
            <input class="form-control" ng-model="todo.isDone" type="checkbox" name="done" />
          </label>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <label id='del'>Delete
            <br>
            <button type="button" ng-click="deleteTodo($index)" name="delete"></button>
          </label>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
           <label id='pro'>In Progress
            <br>
            <button type="pro" ng-click="deleteTodo($index)" name="pro" id="progress_status"></button>
          </label>
        </div>
        <div class="col-2" id="list">
          <span class="todoName" @click="showModal = true">{{ item.label }}</span>
          </div>
          <ModalComponent :item="item" v-if="showModal" @close="showModal = false">
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
          label: '',
          progress: true,
          description: '',
          done: false,
          showModal: false,
          task: [
            {
              "label": "test",
              "progress": "in progress"
            }
          ],
          token:document.head.querySelector('meta[name="csrf-token"]').content
        }
        
    },

    created() {
        socket.on('new user')
    },

    methods: {
      addItem() {
        this.task.push({
          label : this.label,
          description: this.description,
          progress: this.progress, 
          done: this.done
        });
        this.label = ""
        this.description = ""
      },

      fetchItemList() {
        axios.get('/api/todolist/'+ this.user.name).then(response => {
          this.task = response.data;
        });
      },

      deleteAll() {
        
      },
      deleteItem() {

      }
    }

}
    
</script>
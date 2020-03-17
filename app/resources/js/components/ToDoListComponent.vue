<template>
    <div class="container" id="wrapper">
         <form name="createForm" class="form" novalidate>
             <h1>Welcome back, {{ user.name }}! What would you like to do today?</h1>
             <section class="row">
            <div class="col-1" id="addTask">
            <input class="form-control" type="text" data-ng-model="newTodo.Name" placeholder="I Need To..." required />
            <button class="add" ng-click="addTodo(newTodo)" data-ng-disabled="createForm.$invalid">➕</button>
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
          <button class='control' data-ng-click="markAllDone()" data-ng-disabled="!almostOneNotDone()">Mark All Completed</button>
        </div>
         <div class="col-1">
          <button class='control' data-ng-click="uncheckAllDone()" data-ng-disabled="!doneCount()>0">Unmark All Completed</button>
        </div>
        <div class="col-1">
          <button class='control' data-ng-click="deleteAll()" data-ng-disabled="!todos.length">Delete All</button>
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
          <span class="todoName text-center">Good Job! All Tasks Are Complete.</span>
        </div>
      </section>
       <section class="row" ng-repeat="todo in todos | filter:todoSearch.name" ng-class="{'todoItem-done': todo.isDone, 'todoItem-toDo': !todo.isDone}">
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
            <button type="button" ng-click="deleteTodo($index)" name="pro"></button>
          </label>
        </div>
        <div class="col-2" id="list">
          <span class="todoName"></span>
          </div>
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


export default {
    props: ['user'],

    data() {
        return{
        task: []
        }
        
    },
    created() {
        socket.on('new user')
    },
    methods: {

    }

}
    
</script>
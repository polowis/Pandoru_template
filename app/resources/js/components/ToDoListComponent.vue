<template>
    <div class="container" id="wrapper">
         <form name="createForm" class="form" novalidate>
             <h1 class="rainbow">Welcome back, {{ user.name }}! What would you like to do today?</h1>
             <section class="row">
            <div class="col-1" id="addTask">
            <input class="form-control" type="text"  v-model="title" placeholder="Give your task a title" required />
            <input class="form-control" type="text" v-model="description" placeholder="I need to..." required />
              <button class="add" @click.prevent="addItem" :disabled="invalidSubmit()">➕</button>
            </div>
             <div class="col-1" id="search">
          <input type="text" class="form-control" v-model="search" placeholder=" Search Tasks   🔎" />
        </div>
             </section>
         <section class="row" id='actions'>
        <div class="col-1">
          <button class='control'  @click.prevent="deleteComplete()" :disabled="this.task.length == 0 ">Delete Completed</button>
        </div>
         <div class="col-1">
          <button class='control' @click.prevent="markAllDone()" :disabled="this.task.length == 0 ">Mark All Completed</button>
        </div>
         <div class="col-1">
          <button class='control' @click.prevent="uncheckAllDone()" :disabled="this.task.length == 0 ">Unmark All Completed</button>
        </div>
        <div class="col-1">
          <button class='control' @click.prevent="deleteAll()" :disabled="this.task.length == 0 ">Delete All</button>
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
       <section class="row" v-for="item in filter" :key="item.id">
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
          <span class="todoName"  :class="{toDoLineDone: item.done}" @click.prevent="show(item.id)">{{ item.title }}</span>
          </div>
          <div class="col-2" id="list">
            <span class="todoname" :class="{toDoLineDone: item.done}">{{ item.description }}</span>
          </div> 
          <modal :name="item.id.toString()" transition="pop-out" :width="656" :height="400">
            
             <div class="box">
    <div class="box-part" id="bp-left">
      <div class="partition" id="partition-register">
        <div class="partition-title">{{ item.title }}</div>
        <div class="partition-form">
          <form autocomplete="false">

            <div class="autocomplete-fix">
              <input type="password">
            </div>

            <input id="n-title" type="text" placeholder="Title" :value="item.title">
            <input id="n-description" type="text" placeholder="Description" :value="item.description">
            <!--<input id="n-password2" type="password" placeholder="Password">-->
          </form>

          <div style="margin-top: 42px">
          </div>

          <button class="large-btn github-btn" @click.prevent="deleteItem(item)">Click to <span>delete</span></button>
          <button class="large-btn facebook-btn" @click.prevent="editItem(item)">Click to <span>edit</span></button>
        </div>
      </div>
    </div>
    <div class="box-part" id="bp-right">
      <div class="box-messages">
      </div>
    </div>
  </div>
          </modal>
          
          <!--<ModalComponent :items="item" v-if="showModal" :title="item.title" :desc="item.description" @close="showModal = false">
            
      </ModalComponent>-->
          </section>  
          <section class = 'row' id = 'cls'>
           <div class = "col-2" >
             <!--
            <button @click="gobackHome()">Go to home page</button>
             -->
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
          room: this.user.name + this.user.email,
          search: '',
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
        //let room = this.user.name + this.user.email
        socket.emit('privateroom', this.user.name+this.user.email)
        socket.on('update list', (tasks) => {
          this.task = tasks
        })
    },

    computed: {
      filter(){
        if(this.search.length >= 1){
          return this.task.filter((item) => {
            return item.title.startsWith(this.search);
          })
          
        }
        else{
            return this.task
          }
      }
    },

    methods: {
      gobackHome()
      {
        window.location.href = '/'
      },
      show(name){
        this.$modal.show(name.toString(), {
        title: 'Alert!',
        text: 'You are too awesome',
        buttons: [
          {
            title: 'Deal with it',
            handler: () => { alert('Woot!') }
          },
          {
            title: '',       // Button title
            default: true,    // Will be triggered by default if 'Enter' pressed.
            handler: () => {} // Button click handler
          },
          {
            title: 'Close'
          }
      ]
      })
      },


      hide(name){
        this.$modal.hide(name.toString())
      },


      editItem(item)
      {
        let itemElement = this.task[this.task.indexOf(item)]
        let title = document.getElementById('n-title').value
        let description = document.getElementById('n-description').value

        axios.post('/api/'+ itemElement.id, {
          title: title,
          description: description
        }).then(response => {
          itemElement.title = title
          itemElement.description = description
          this.hide(itemElement.id)
        })

      },

      uncheckAllDone(){
         for(let item = 0; item < this.task.length; item++) {
            if(this.task[item].done == true || this.task[item].done == 1){
                axios.post('/api/undone/' + this.task[item].id).then(response => {
                  if(response.data.message == 'Success'){
                  this.task[item].done = false;
                  this.task[item].progress = true;
                  socket.emit('update list', {task: this.task, room: this.room})
                  }

              }).then((res) =>{

              }).catch(error =>{
                      
              });
                }
          }
      },
      
      deleteItemByButton(item_id){
        axios.post('/api/delete/' + item_id).then(response => {
          this.task.splice(item_id, 1)
          this.$emit('close')
        }).then((res) =>{

        }).catch(error =>{
                
        });
      },

      
      addItem() {
        
        axios.post('/api/create', {title: this.title, description: this.description, progress: this.progress}).then(response => {
           if(response.data.message == 'Success'){
            this.task.push({
              id: response.data.id,
              title: response.data.title,
              description: response.data.description,
              done: response.data.done,
              progress: response.data.progress,
            })

            this.title = ""
            this.description = ""
            socket.emit('update list', {task: this.task, room: this.room})
        }}).then((res) =>{

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
              if(response.data.message == 'Success'){
              this.task = []
              socket.emit('update list', {task: this.task, room: this.room})

          }}).then((res) =>{

          }).catch(error =>{
                  
          });
          }
          
      },

      deleteItem(item) {
        let item_id = this.task[this.task.indexOf(item)].id
        axios.post('/api/delete/' + item_id).then(response => {
          if(response.data.message == 'Success'){
          this.task.splice(this.task.indexOf(item), 1)
          this.hide(item_id)
          socket.emit('update list', {task: this.task, room: this.room})
        }}).then((res) =>{

        }).catch(error =>{
                
        });
        
        
      },

      markItemAsDone(item)
      {
        let item_element = this.task[this.task.indexOf(item)]
        axios.post('/api/done/' + item_element.id).then(response => {
          if(response.data.message == 'Success'){
          item_element.done = true;
          item_element.progress = false;
          socket.emit('update list', {task: this.task, room: this.room})
          
        }}).then((res) =>{

        }).catch(error =>{
                
        });
      },

      invalidSubmit(){
        let valid_letters = /^[a-z\d\-_\s]+$/i
       if(this.title.match(valid_letters) && this.description.match(valid_letters)){
         return false;
       } else{
         return true;
       }
      },

      markAllDone()
      {
        for(let item = 0; item < this.task.length; item++){
           axios.post('/api/done/' + this.task[item].id).then(response => {
           if(response.data.message == 'Success'){
            this.task[item].done = true;
            this.task[item].progress = false;
            socket.emit('update list', {task: this.task, room: this.room})
          }}).then((res) =>{

          }).catch(error =>{
                  
          });
        }
        
         
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
                 if(response.data.message == 'Success'){
                  this.task.splice(item, 1)
                  socket.emit('update list', {task: this.task, room: this.room})

              }}).then((res) =>{

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
<style lang="scss">
$background_color: #404142;
$github_color: #DBA226;
$facebook_color: #3880FF;
.box {
  background: white;
  overflow: hidden;
  width: 656px;
  height: 400px;
  border-radius: 2px;
  box-sizing: border-box;
  box-shadow: 0 0 40px black;
  color: #8b8c8d;
  font-size: 0;
  .box-part {
    display: inline-block;
    position: relative;
    vertical-align: top;
    box-sizing: border-box;
    height: 100%;
    width: 50%;
    &#bp-right {
      background: url("https://www.thecoderpedia.com/wp-content/uploads/2019/09/programming-3652497_1920.jpg") no-repeat top left;
      border-left: 1px solid #eee;
    }
  }
  .box-messages {
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
  }
  .box-error-message {
    position: relative;
    overflow: hidden;
    box-sizing: border-box;
    height: 0;
    line-height: 32px;
    padding: 0 12px;
    text-align: center;
    width: 100%;
    font-size: 11px;
    color: white;
    background: #F38181;
  }
  .partition {
    width: 100%;
    height: 100%;
    .partition-title {
      box-sizing: border-box;
      padding: 30px;
      width: 100%;
      text-align: center;
      letter-spacing: 1px;
      font-size: 20px;
      font-weight: 300;
    }
    .partition-form {
      padding: 0 20px;
      box-sizing: border-box;
    }
  }
  input[type=password],
  input[type=text] {
    display: block;
    box-sizing: border-box;
    margin-bottom: 4px;
    width: 100%;
    font-size: 12px;
    line-height: 2;
    border: 0;
    border-bottom: 1px solid #DDDEDF;
    padding: 4px 8px;
    font-family: inherit;
    transition: 0.5s all;
    outline: none;
  }
  button {
    background: white;
    border-radius: 4px;
    box-sizing: border-box;
    padding: 10px;
    letter-spacing: 1px;
    font-family: "Open Sans", sans-serif;
    font-weight: 400;
    min-width: 140px;
    margin-top: 8px;
    color: #8b8c8d;
    cursor: pointer;
    border: 1px solid #DDDEDF;
    text-transform: uppercase;
    transition: 0.1s all;
    font-size: 10px;
    outline: none;
    &:hover {
      border-color: mix(#DDDEDF, black, 90%);
      color: mix(#8b8c8d, black, 80%);
    }
  }
  .large-btn {
    width: 100%;
    background: white;
    span {
      font-weight: 600;
    }
    &:hover {
      color: white !important;
    }
  }
  .button-set {
    margin-bottom: 8px;
  }
  #register-btn,
  #signin-btn {
    margin-left: 8px;
  }
  .facebook-btn {
    border-color: $facebook_color;
    color: $facebook_color;
    &:hover {
      border-color: $facebook_color;
      background: $facebook_color;
    }
  }
  .github-btn {
    border-color: $github_color;
    color: $github_color;
    &:hover {
      border-color: $github_color;
      background: $github_color;
    }
  }
  .autocomplete-fix {
    position: absolute;
    visibility: hidden;
    overflow: hidden;
    opacity: 0;
    width: 0;
    height: 0;
    left: 0;
    top: 0;
  }
}
.pop-out-enter-active,
.pop-out-leave-active {
  transition: all 0.5s;
}
.pop-out-enter,
.pop-out-leave-active {
  opacity: 0;
  transform: translateY(24px);
}
</style>
<template>
    <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-container">

              <div class="modal-header">
                <slot name="header">
                  <strong>{{ title }}</strong>
                </slot>
              </div>

              <div class="modal-body">
                <slot name="body">
                  {{ desc }}
                </slot>
              </div>

              <div class="modal-footer">
                <slot name="footer">
                  
                  {{items.progress}}
                  <button class="modal-default-button btn btn-success" @click.prevent="$emit('close')">
                    OK
                  </button>
                </slot>
              </div>
            </div>
          </div>
        </div>
      </transition>
</template>
<script>
export default {
    props: ['user', 'items', 'showModal', 'title', 'desc'],
    methods:{
      getItem(item) {
        console.log(items)
      }
    }
}

</script>

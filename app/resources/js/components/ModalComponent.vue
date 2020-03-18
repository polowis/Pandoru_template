<template>
    <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-container">

              <div class="modal-header">
                <slot name="header">
                  <strong>{{item.title}}</strong>
                </slot>
              </div>

              <div class="modal-body">
                <slot name="body">
                  {{item.description}}
                </slot>
              </div>

              <div class="modal-footer">
                <slot name="footer">
                  
                  {{item.progress}}
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
    props: ['user', 'item', 'showModal']
}
</script>

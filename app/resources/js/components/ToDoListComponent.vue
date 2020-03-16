<template>
    
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
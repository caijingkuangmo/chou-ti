<template>
  <div class="cc-video">
    <el-dialog :visible="dialogVisible" :show-close="true" width="923px" :before-close="handleClose">
      <object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,0,0"
        width="930" height="580" :id="`cc_${ccid}`">
        <param name="movie" :value="`https://p.bokecc.com/flash/single/D526608623AF083F_${ccid}_false_C57B331506413D8F_1/player.swf`" />
        <param name="allowFullScreen" value="true" />
        <param name="allowScriptAccess" value="always" />
        <param value="transparent" name="wmode" /><embed :src="`https://p.bokecc.com/flash/single/D526608623AF083F_${ccid}_false_C57B331506413D8F_1/player.swf`"
          width="923" height="580" :name="`cc_${ccid}`" allowFullScreen="true" wmode="transparent" allowScriptAccess="always"
          pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" /></object>
    </el-dialog>
  </div>


</template>

<script>
  export default {
    name: "cc-video",
    data() {
      return {
        ccid: "FB68BE1CFB9D3BC19C33DC5901307461",
        dialogVisible: false,
      }
    },
    methods: {
      handleClose(done) {
        this.dialogVisible = false;
      },
      showDialog() {
        this.dialogVisible = true;
      }
    },

  }

</script>

<style>
  .cc-video .el-dialog__header {
    padding: 0;
  }

  .cc-video .el-dialog__body {
    padding: 0;
  }

</style>

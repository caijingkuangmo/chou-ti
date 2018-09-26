<template>
    <div>
        <el-dialog
            title="分享新发现"
            :visible="dialogVisible"
            width="50%"
            :before-close="handleClose">
            <PublishTab></PublishTab>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">清空</el-button>
                <el-button type="primary" @click="dialogVisible = false">发布</el-button>
            </span>
            </el-dialog>
    </div>
</template>

<script>
import PublishTab from "./publish-tab.vue";

export default {
  name: "PublishNewsDialog",
  data() {
    return {
      dialogVisible: false
    };
  },
  methods: {
    handleClose(done) {
      this.dialogVisible = false;
    },
    showDialog() {
      this.dialogVisible = true;
    }
  },
  components: {
    PublishTab
  }
};
</script>

<style scoped>
</style>



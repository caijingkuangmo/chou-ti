<template>
    <div id="publish-tab">
        <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
            <el-tab-pane label="链接" name="first">
              <el-form ref="linkForm" :model="linkForm" label-width="80px">
                <el-form-item label="添加链接">
                  <el-input v-model="linkForm.addLink"></el-input>
                </el-form-item>
                <el-form-item label="标题">
                  <el-input v-model="linkForm.title"></el-input>
                </el-form-item>
                <el-form-item label="添加摘要(选填)">
                  <el-input type="textarea" v-model="linkForm.summary"></el-input>
                </el-form-item>
                <el-form-item label="发布到：">
                  <el-radio-group v-model="linkForm.type">
                    <el-radio label="42区"></el-radio>
                    <el-radio label="段子"></el-radio>
                    <el-radio label="图片"></el-radio>
                    <el-radio label="挨踢1024"></el-radio>
                    <el-radio label="你问我答"></el-radio>
                  </el-radio-group>
                </el-form-item>
              </el-form>
            </el-tab-pane>
            <el-tab-pane label="文字" name="second">
              <el-form ref="wordForm" :model="wordForm" label-width="80px">
                <el-form-item>
                  <el-input type="textarea" v-model="wordForm.context"></el-input>
                </el-form-item>
                <el-form-item label="发布到：">
                  <el-radio-group v-model="wordForm.type">
                    <el-radio label="段子"></el-radio>
                    <el-radio label="你问我答"></el-radio>
                  </el-radio-group>
                </el-form-item>
              </el-form>
            </el-tab-pane>
            <el-tab-pane label="图片" name="third">
              <el-form ref="imageForm" :model="imageForm" label-width="80px">
                <el-form-item label="添加图片">
                  <el-upload
                    class="upload-demo"
                    action="/flask-api/hello/upload"
                    :on-preview="handlePreview"
                    :on-remove="handleRemove"
                    :file-list="fileList2"
                    list-type="picture">
                    <el-button size="small" type="primary">点击上传</el-button>
                    <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
                  </el-upload>
                </el-form-item>
                <el-form-item>
                  <el-input type="textarea" v-model="imageForm.title"></el-input>
                </el-form-item>
                <el-form-item label="发布到：">
                  <el-radio-group v-model="imageForm.type">
                    <el-radio label="图片"></el-radio>
                    <el-radio label="你问我答"></el-radio>
                  </el-radio-group>
                </el-form-item>
              </el-form>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
export default {
  name: "PublishTab",
  data() {
    return {
      activeName: "first",
      fileList2: [],
      linkForm:{
        addLink:"",
        title:"",
        summary:"",
        type:"42区"
      },
      wordForm:{
        content:"",
        type:"段子"
      },
      imageForm:{
        title:"",
        type:"图片"
      }
    };
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    }
  }
};
</script>

<style>
#publish-tab .el-upload__input{
  display: none !important;
}
</style>


<style scoped>

</style>



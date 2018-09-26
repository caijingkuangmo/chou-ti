<template>
    <div id="content-area">
        <div class="filter-bar">
            <span class="hot">
                <span :class="{hotSelect:hostSel=='hot'}" @click="hostSel='hot'">最热</span>
                <span :class="{hotSelect:hostSel=='discovery'}" @click="hostSel='discovery'">发现</span>
                <span :class="{hotSelect:hostSel=='human'}" @click="hostSel='human'">人类发布</span>
            </span>
            <span class="immediately">
                <span :class="{timeSelect:timeSel=='immediately'}" @click="timeSel='immediately'">即时排序</span>
                <span :class="{timeSelect:timeSel=='hours'}" @click="timeSel='hours'">24小时</span>
                <span :class="{timeSelect:timeSel=='days'}" @click="timeSel='days'">3天</span>
            </span>
            <span class="publish">
                <el-button icon="el-icon-plus" type="primary" @click="publish">发布</el-button>
            </span>
        </div>
        <ContentItem v-for="news in newsList" :key="news.id" :news="news"></ContentItem>
        <PublishNewsDialog ref="publishDialog"></PublishNewsDialog>
    </div>
</template>

<script>
import ContentItem from "./content-item.vue";
import PublishNewsDialog from "./publish-news-dialog.vue";

export default {
  name: "ContentDisplayArea",
  data() {
    return {
      hostSel: "hot",
      timeSel: "immediately",
      newsList: this.$store.state.user.newsList
    };
  },
  methods: {
    publish() {
      this.$refs["publishDialog"].showDialog();
    }
  },
  components: {
    ContentItem,
    PublishNewsDialog
  }
};
</script>

<style scoped>
#content-area {
  width: 980px;
  margin: 0 auto;
}

.filter-bar {
  height: 50px;
  line-height: 50px;
  font-size: 14px;
  margin-left: 30px;
  border-bottom: 1px gray solid;
}

.hot span {
  display: inline-block;
  padding-left: 10px;
  padding-right: 10px;
  line-height: 30px;
  font-weight: 700;
  cursor: pointer;
}

.hotSelect {
  border-radius: 20px;
  background: rgb(240, 244, 248);
  border: solid 1px #eee;
}

.immediately {
  margin-left: 200px;
}

.immediately span {
  color: rgb(132, 164, 43);
  cursor: pointer;
  margin-left: 10px;
}

.timeSelect {
  color: rgb(180, 180, 180) !important;
}

.publish {
  margin-left: 30px;
}
</style>



<template>
    <div class="news-content-item">
        <div class="news-content">
            <div class="title-content">
                <div>
                    <span class="news-title">{{news.title}}</span>
                    <span class="news-website">{{news.website}}</span>
                    <span class="news-type">{{news.type}}</span>
                    <span class="news-device">{{news.device}}</span>
                </div>
                <div class="news-describe">
                    {{news.describe}}
                </div>
            </div>
            <div class="picture">
                <img :src="`${news.picture}`" class="news-picture">
            </div>
        </div>
        <div class="operations">
            <span class="favor">
                <span class="digg-a">
                    <span class="hand-icon icon-favor"></span>
                    <b class="nums">{{news.favorNum}}</b>
                </span>
                <span class="digg-a" @click="showComment">
                    <span class="hand-icon icon-comment"></span>
                    <b class="nums">{{news.commentNum}}</b>
                </span>
                <span class="digg-a">
                    <span class="hand-icon icon-collect"></span>
                </span>
            </span>
            <span class="news-resource">
                <img :src="`${news.publishLogo}`" class="imgs">
                <span class="publish-name">{{news.publisher}}</span>
                <span class="publish-time-info">
                    <span class="publish-time">{{news.publishTime}}</span>
                    <span>入热搜</span>
                </span>
            </span>
            <span class="share">
                分享到
                <span class="weibo"></span>
                <span class="douban"></span>
                <span class="kongjian"></span>
                <span class="renren"></span>
            </span>
            <CommentBox :comments='news.commentList' :commentNum="news.commentNum" ref="commentBox"></CommentBox>
        </div>
    </div>
</template>

<script>
import CommentBox from "./comment-box.vue";

export default {
  name: "ContentItem",
  props: ["news"],
  data() {
    return {};
  },
  methods: {
    showComment() {
      this.$refs["commentBox"].showComment();
    }
  },
  components: {
    CommentBox
  }
};
</script>

<style scoped>
.news-content-item {
  margin-top: 15px;
  margin-left: 30px;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
}

.title-content {
  width: 860px;
  display: inline-block;
  vertical-align: top;
}

.picture {
  margin-left: 5px;
  margin-top: 15px;
  width: 80px;
  display: inline-block;
}

.news-title {
  font-size: 20px;
  color: #369;
  font-weight: 700;
  word-wrap: break-word;
  word-break: break-all;
  overflow: hidden;
}

.news-title:hover {
  text-decoration: underline;
  cursor: pointer;
}

.news-website {
  color: #b4b4b4;
  margin-left: 7px;
}

.news-type {
  color: #b4b4b4;
  margin-left: 7px;
  cursor: pointer;
  text-decoration: underline;
}

.news-device {
  color: #b4b4b4;
  margin-left: 13px;
}

.news-describe {
  line-height: 20px;
  font-size: 12px;
  color: #787878;
  font-family: Arial, Helvetica, sans-serif;
  word-wrap: break-word;
  word-break: break-all;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  margin-top: 5px;
}

.news-picture {
  width: 60px;
  height: 60px;
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 1px;
  vertical-align: top;
}

.operations {
  margin-top: 7px;
}

.hand-icon {
  background: url("./../../assets/icon.png") no-repeat 0 0;
}
.icon-favor {
  background-position: 0 -40px;
  width: 18px;
  height: 18px;
  display: inline-block;
  vertical-align: bottom;
}

.icon-comment {
  background-position: 0 -100px;
  width: 18px;
  height: 18px;
  display: inline-block;
  vertical-align: bottom;
}

.icon-collect {
  background-position: 0 -160px;
  width: 18px;
  height: 18px;
  display: inline-block;
  vertical-align: bottom;
}

.digg-a {
  cursor: pointer;
  display: inline-block;
  min-width: 54px;
}

.nums {
  margin-left: 3px;
  color: rgb(192, 203, 217);
}

.icon-favor:hover {
  background-position: 0 -20px;
  cursor: pointer;
}

.icon-comment:hover {
  background-position: 0 -80px;
  cursor: pointer;
}

.icon-collect:hover {
  background-position: 0 -140px;
  cursor: pointer;
}

.nums:hover {
  color: black;
  text-decoration: underline;
  cursor: pointer;
}

.news-resource {
  margin-left: 30px;
}

.imgs {
  width: 18px;
  height: 18px;
  display: inline-block;
  vertical-align: bottom;
}

.publish-name {
  font-family: "仿宋";
  margin-left: 3px;
  color: rgb(153, 174, 203);
}

.publish-name:hover {
  color: black;
  text-decoration: underline;
  cursor: pointer;
}

.publish-time-info {
  font-size: 14px;
  color: rgb(153, 174, 203);
  margin-left: 15px;
}

.publish-time {
  color: rgb(230, 147, 115);
}

.publish-time:hover {
  text-decoration: underline;
  cursor: pointer;
}

.share {
  margin-left: 30px;
  font-family: "仿宋";
  font-size: 14px;
  opacity: 0;
}

.share:hover {
  opacity: 1;
}

.share span {
  display: inline-block;
  width: 17px;
  height: 14px;
  background-image: url("./../../assets/share_icon.png");
  background-repeat: no-repeat;
}

.weibo {
  background-position: 0 0;
}

.douban {
  background-position: 0 -15px;
}

.kongjian {
  background-position: 0 -30px;
}
.renren {
  background-position: 0 -60px;
}

.weibo:hover {
  background-position: 0 -90px;
  cursor: pointer;
}

.douban:hover {
  background-position: 0 -104px;
  cursor: pointer;
}
.kongjian:hover {
  background-position: 0 -120px;
  cursor: pointer;
}
.renren:hover {
  background-position: 0 -150px;
  cursor: pointer;
}
</style>



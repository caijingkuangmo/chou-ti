<template>
  <div>
    <div class="brief-area">
      <span class="brief-title">课程概述</span>
      <div>信息时代，数据为王，互联网包含了迄今为止最有用的数据集，并且大部分可以免费公开访问，但是由于数据被嵌入在众多网站的结构和样式中导致难以被复用，应运而生出现了网络爬虫，使用程序自动获取互联网上的资源。本系列课程将带你开发自动化程序实现数据自动采集，针对众多网站防止数据被获取采取防爬虫方案，课程中包含对防爬策略所有解决方法，专治各种爬虫疑难杂症，同时课程还从源码级别深度剖析流行的爬虫框架，研究如何提高爬虫性能，使你在爬虫方向真正做到“遇鬼杀鬼，遇神杀神，所向披靡”。</div>
      <img src="@/assets/python.png" alt="">
    </div>
    <div class="price-area">
        <el-row>
            <el-col v-for="(val, index) in [1,2,3,4]" :key="index" :span="3" :offset="2">
                <div style="height:110px;width:220px;border: 1px solid #eee;text-align:center">
                    <div style="margin-top:15px;">￥ 99</div>
                    <div style="margin-top:10px;">有效期1个月</div>
                </div>
            </el-col>
        </el-row>
        <div style="width:100%;text-align:center;margin-top:30px;">
            <el-button type="primary" size="medium">购买</el-button>
            <el-button type="success" size="medium" style="margin-left:30px;">加入购物车</el-button>
        </div>
    </div>
  </div>
</template>

<script>
  import PlayPng from "@/assets/play.png"

  export default {
    name: "course-item-overview",
    data() {
      return {

      }
    }
  }

</script>

<style scoped>
  .brief-area div {
    width: 50%;
    display: inline-block;
    margin-left: 10%;
  }

  .brief-area img {
    display: inline-block;
    width: 20%;
    margin-left: 10%;
    height: 120px;
    vertical-align: bottom;
  }

  .brief-title {
    margin-top: 20px;
    margin-left: 10%;
    font-size: 42px;
    font-weight: bold;
    display: block;
  }

.price-area{
    margin:5%;
    font-size:24px;
    font-weight: bold;
}
</style>

  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>device-sony-lt26/tools/mkelf.py at master · sonyxperiadev/device-sony-lt26 · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon-precomposed" sizes="57x57" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="apple-touch-icon-144.png" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="apple-touch-icon-144.png" />
    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="6FCP4wpLSt3NGwujwI/BRsGCPgcbTxnMTYYAjx/xZmY=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-ed9200b8b8863732315786682f52566d65622837.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-37f887f5d0cc1ca1790f28b826acc90e7bf52a62.css" media="screen" rel="stylesheet" type="text/css" />
    


    <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-eee761b9d5e06efb064aaaf528c44ef8e1601e71.js" type="text/javascript"></script>
    <script src="https://a248.e.akamai.net/assets.github.com/assets/github-d035b9b578d1adc2c70dd2d4c44329f16450842f.js" type="text/javascript"></script>
    

        <link rel='permalink' href='/sonyxperiadev/device-sony-lt26/blob/d4a99647d5868aa0503940ea0b0bdd8bc2fa613d/tools/mkelf.py'>
    <meta property="og:title" content="device-sony-lt26"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/sonyxperiadev/device-sony-lt26"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/0be131c9d3fb779490e90ca8a38f03e8?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="Android device configuration for Xperia S. Contribute to device-sony-lt26 development by creating an account on GitHub."/>

    <meta name="description" content="Android device configuration for Xperia S. Contribute to device-sony-lt26 development by creating an account on GitHub." />

  <link href="https://github.com/sonyxperiadev/device-sony-lt26/commits/master.atom" rel="alternate" title="Recent Commits to device-sony-lt26:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob  vis-public env-production ">
    <div id="wrapper">

      

      

      


        <div class="header header-logged-out">
          <div class="container clearfix">

            <a class="header-logo-wordmark" href="https://github.com/">
              <img alt="GitHub" class="github-logo-4x" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x.png?1337118066" />
              <img alt="GitHub" class="github-logo-4x-hover" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x-hover.png?1337118066" />
            </a>

              
<ul class="top-nav">
    <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
  <li class="search"><a href="https://github.com/search">Search</a></li>
  <li class="features"><a href="https://github.com/features">Features</a></li>
    <li class="blog"><a href="https://github.com/blog">Blog</a></li>
</ul>


            <div class="header-actions">
                <a class="button primary classy" href="https://github.com/signup">Sign up for free</a>
              <a class="button classy" href="https://github.com/login?return_to=%2Fsonyxperiadev%2Fdevice-sony-lt26%2Fblob%2Fmaster%2Ftools%2Fmkelf.py">Sign in</a>
            </div>

          </div>
        </div>


      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu">
          <div class="container">
            <div class="title-actions-bar">
              


                  <ul class="pagehead-actions">


          <li>
            <span class="star-button"><a href="/login?return_to=%2Fsonyxperiadev%2Fdevice-sony-lt26" class="minibutton js-toggler-target entice tooltipped leftwards" title="You must be signed in to use this feature" rel="nofollow"><span class="mini-icon mini-icon-star"></span>Star</a><a class="social-count js-social-count" href="/sonyxperiadev/device-sony-lt26/stargazers">45</a></span>
          </li>
          <li>
            <a href="/login?return_to=%2Fsonyxperiadev%2Fdevice-sony-lt26" class="minibutton js-toggler-target fork-button entice tooltipped leftwards"  title="You must be signed in to fork a repository" rel="nofollow"><span class="mini-icon mini-icon-fork"></span>Fork</a><a href="/sonyxperiadev/device-sony-lt26/network" class="social-count">14</a>
          </li>
    </ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-icon mega-icon-public-repo"></span>
                <span class="author vcard">
                  <a href="/sonyxperiadev" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">sonyxperiadev</span>
                  </a></span> /
                <strong><a href="/sonyxperiadev/device-sony-lt26" class="js-current-repository">device-sony-lt26</a></strong>
              </h1>
            </div>

            

  <ul class="tabs">
    <li><a href="/sonyxperiadev/device-sony-lt26" class="selected" highlight="repo_sourcerepo_downloadsrepo_commitsrepo_tagsrepo_branches">Code</a></li>
    <li><a href="/sonyxperiadev/device-sony-lt26/network" highlight="repo_network">Network</a></li>
    <li><a href="/sonyxperiadev/device-sony-lt26/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>1</span></a></li>

      <li><a href="/sonyxperiadev/device-sony-lt26/issues" highlight="repo_issues">Issues <span class='counter'>2</span></a></li>



    <li><a href="/sonyxperiadev/device-sony-lt26/graphs" highlight="repo_graphsrepo_contributors">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
      <li><a href="/sonyxperiadev/device-sony-lt26/tags" class="tabnav-tab" highlight="repo_tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
    
  </span>

  <div class="tabnav-widget scope">


    <div class="context-menu-container js-menu-container js-context-menu">
      <a href="#"
         class="minibutton bigger switcher js-menu-target js-commitish-button btn-branch repo-tree"
         data-hotkey="w"
         data-ref="master">
         <span><em class="mini-icon mini-icon-branch"></em><i>branch:</i> master</span>
      </a>

      <div class="context-pane commitish-context js-menu-content">
        <a href="#" class="close js-menu-close"><span class="mini-icon mini-icon-remove-close"></span></a>
        <div class="context-title">Switch branches/tags</div>
        <div class="context-body pane-selector commitish-selector js-navigation-container">
          <div class="filterbar">
            <input type="text" id="context-commitish-filter-field" class="js-navigation-enable js-filterable-field" placeholder="Filter branches/tags">
            <ul class="tabs">
              <li><a href="#" data-filter="branches" class="selected">Branches</a></li>
                <li><a href="#" data-filter="tags">Tags</a></li>
            </ul>
          </div>

          <div class="js-filter-tab js-filter-branches">
            <div data-filterable-for="context-commitish-filter-field" data-filterable-type=substring>
                <div class="commitish-item branch-commitish selector-item js-navigation-item js-navigation-target selected">
                  <span class="mini-icon mini-icon-confirm"></span>
                  <h4>
                      <a href="/sonyxperiadev/device-sony-lt26/blob/master/tools/mkelf.py" class="js-navigation-open" data-name="master" rel="nofollow">master</a>
                  </h4>
                </div>
            </div>
            <div class="no-results">Nothing to show</div>
          </div>

            <div class="js-filter-tab js-filter-tags filter-tab-empty" style="display:none">
              <div data-filterable-for="context-commitish-filter-field" data-filterable-type=substring>
              </div>
              <div class="no-results">Nothing to show</div>
            </div>
        </div>
      </div><!-- /.commitish-context-context -->
    </div>
  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/sonyxperiadev/device-sony-lt26" class="selected tabnav-tab" highlight="repo_source">Files</a></li>
    <li><a href="/sonyxperiadev/device-sony-lt26/commits/master" class="tabnav-tab" highlight="repo_commits">Commits</a></li>
    <li><a href="/sonyxperiadev/device-sony-lt26/branches" class="tabnav-tab" highlight="repo_branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:ffdf6cb8e47fb66d826711b1e2b93f30 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:ffdf6cb8e47fb66d826711b1e2b93f30 -->

<div id="slider">


    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>
      <div class="breadcrumb">
        <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/sonyxperiadev/device-sony-lt26" class="js-slide-to" data-direction="back" itemscope="url"><span itemprop="title">device-sony-lt26</span></a></span></span> / <span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/sonyxperiadev/device-sony-lt26/tree/master/tools" class="js-slide-to" data-direction="back" itemscope="url"><span itemprop="title">tools</span></a></span> / <strong class="final-path">mkelf.py</strong> <span class="js-clippy mini-icon mini-icon-clippy " data-clipboard-text="tools/mkelf.py" data-copied-hint="copied!" data-copy-hint="copy to clipboard"></span>
      </div>

      <a href="/sonyxperiadev/device-sony-lt26/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>

        
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/7319b6bdb0d2892048dc7ee392cf43d7?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><a href="/freexperia" rel="author">freexperia</a></span>
    <time class="js-relative-date" datetime="2012-08-23T00:42:52-07:00" title="2012-08-23 00:42:52">August 23, 2012</time>
    <div class="commit-title">
        <a href="/sonyxperiadev/device-sony-lt26/commit/b644924c93b3c89e0e6f3aeeb85fb9a23147350f" class="message">lt26: enable building custom boot.elf</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2>Users on GitHub who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/7319b6bdb0d2892048dc7ee392cf43d7?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/freexperia">freexperia</a>
        </li>
      </ul>
    </div>
  </div>


    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/sonyxperiadev/device-sony-lt26/blob/d4a99647d5868aa0503940ea0b0bdd8bc2fa613d/tools/mkelf.py" data-title="device-sony-lt26/tools/mkelf.py at master · sonyxperiadev/device-sony-lt26 · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">executable file</span>
                  <span>190 lines (167 sloc)</span>
                <span>6.152 kb</span>
              </div>
              <ul class="button-group actions">
                  <li>
                      <a class="grouped-button minibutton bigger lighter js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  </li>
                <li><a href="/sonyxperiadev/device-sony-lt26/raw/master/tools/mkelf.py" class="minibutton grouped-button bigger lighter" id="raw-url">Raw</a></li>
                  <li><a href="/sonyxperiadev/device-sony-lt26/blame/master/tools/mkelf.py" class="minibutton grouped-button bigger lighter">Blame</a></li>
                <li><a href="/sonyxperiadev/device-sony-lt26/commits/master/tools/mkelf.py" class="minibutton grouped-button bigger lighter" rel="nofollow">History</a></li>
              </ul>
            </div>
                <div class="data type-python">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
</pre>
          </td>
          <td width="100%">
                <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><span class="c">#</span></div><div class='line' id='LC3'><span class="c"># Copyright (c) 2012, Sony Mobile Communications AB</span></div><div class='line' id='LC4'><span class="c"># All rights reserved.</span></div><div class='line' id='LC5'><span class="c">#</span></div><div class='line' id='LC6'><span class="c"># Redistribution and use in source and binary forms, with or without</span></div><div class='line' id='LC7'><span class="c"># modification, are permitted provided that the following conditions</span></div><div class='line' id='LC8'><span class="c"># are met:</span></div><div class='line' id='LC9'><span class="c">#    * Redistributions of source code must retain the above copyright</span></div><div class='line' id='LC10'><span class="c">#      notice, this list of conditions and the following disclaimer.</span></div><div class='line' id='LC11'><span class="c">#    * Redistributions in binary form must reproduce the above copyright</span></div><div class='line' id='LC12'><span class="c">#      notice, this list of conditions and the following disclaimer in</span></div><div class='line' id='LC13'><span class="c">#      the documentation and/or other materials provided with the</span></div><div class='line' id='LC14'><span class="c">#      distribution.</span></div><div class='line' id='LC15'><span class="c">#    * Neither the name of Sony Mobile Communications AB nor the names</span></div><div class='line' id='LC16'><span class="c">#      of its contributors may be used to endorse or promote products</span></div><div class='line' id='LC17'><span class="c">#      derived from this software without specific prior written</span></div><div class='line' id='LC18'><span class="c">#      permission.</span></div><div class='line' id='LC19'><span class="c">#</span></div><div class='line' id='LC20'><span class="c"># THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS</span></div><div class='line' id='LC21'><span class="c"># &quot;AS IS&quot; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT</span></div><div class='line' id='LC22'><span class="c"># LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS</span></div><div class='line' id='LC23'><span class="c"># FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE</span></div><div class='line' id='LC24'><span class="c"># COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,</span></div><div class='line' id='LC25'><span class="c"># INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,</span></div><div class='line' id='LC26'><span class="c"># BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS</span></div><div class='line' id='LC27'><span class="c"># OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED</span></div><div class='line' id='LC28'><span class="c"># AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,</span></div><div class='line' id='LC29'><span class="c"># OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT</span></div><div class='line' id='LC30'><span class="c"># OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF</span></div><div class='line' id='LC31'><span class="c"># SUCH DAMAGE.</span></div><div class='line' id='LC32'><span class="c">#</span></div><div class='line' id='LC33'><span class="c"># DESCRIPTION</span></div><div class='line' id='LC34'><span class="c">#</span></div><div class='line' id='LC35'><span class="c">#   Combine one or more files to a elf file.</span></div><div class='line' id='LC36'><span class="c">#</span></div><div class='line' id='LC37'><span class="c"># SYNOPSIS</span></div><div class='line' id='LC38'><span class="c">#</span></div><div class='line' id='LC39'><span class="c">#   mkelf.py -o elf file@addr[,ramdisk] ...</span></div><div class='line' id='LC40'><span class="c">#</span></div><div class='line' id='LC41'><span class="c">#   elf         The path to the output file</span></div><div class='line' id='LC42'><span class="c">#   file        Input file</span></div><div class='line' id='LC43'><span class="c">#   addr        ELF vaddr and paddr of this file</span></div><div class='line' id='LC44'><span class="c">#   ramdisk     Mark this segment to be presented in ATAG list as ramdisk (optional)</span></div><div class='line' id='LC45'><span class="c">#   ipl         Mark this segment to be handled by the boot code as IPL (optional)</span></div><div class='line' id='LC46'><span class="c">#   cmdline     Mark this segment to be handled by the boot code as kernel cmdline (optional)</span></div><div class='line' id='LC47'><span class="c">#</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'><span class="kn">import</span> <span class="nn">re</span></div><div class='line' id='LC50'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC51'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC52'><span class="kn">import</span> <span class="nn">struct</span></div><div class='line' id='LC53'><span class="kn">from</span> <span class="nn">optparse</span> <span class="kn">import</span> <span class="n">OptionParser</span></div><div class='line' id='LC54'><br/></div><div class='line' id='LC55'><span class="c"># Elf definitions</span></div><div class='line' id='LC56'><span class="n">PT_NULL</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC57'><span class="n">PT_LOAD</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC58'><span class="n">PT_NOTE</span> <span class="o">=</span> <span class="mi">4</span></div><div class='line' id='LC59'><br/></div><div class='line' id='LC60'><span class="c"># SEMC Elf definitions</span></div><div class='line' id='LC61'><span class="n">P_FLAGS_RAMDISK</span> <span class="o">=</span> <span class="mh">0x80000000</span></div><div class='line' id='LC62'><span class="n">P_FLAGS_IPL</span>     <span class="o">=</span> <span class="mh">0x40000000</span> <span class="c"># used for STE U8500</span></div><div class='line' id='LC63'><span class="n">P_FLAGS_CMDLINE</span> <span class="o">=</span> <span class="mh">0x20000000</span></div><div class='line' id='LC64'><span class="n">P_FLAGS_RPM</span>     <span class="o">=</span> <span class="mh">0x01000000</span> <span class="c"># used for QCT MSM8x60</span></div><div class='line' id='LC65'><br/></div><div class='line' id='LC66'><span class="k">def</span> <span class="nf">fatal</span><span class="p">(</span><span class="n">message</span><span class="p">):</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span> <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="p">,</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span> <span class="n">message</span><span class="p">)</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'><span class="k">def</span> <span class="nf">parse_inputs</span><span class="p">(</span><span class="n">args</span><span class="p">):</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">segs</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">args</span><span class="p">:</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seg</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tokens</span> <span class="o">=</span> <span class="n">arg</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;@&#39;</span><span class="p">)</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tokens</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">2</span><span class="p">:</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fatal</span><span class="p">(</span><span class="s">&#39;Incorrect format of input parameter: &#39;</span> <span class="o">+</span> <span class="n">arg</span><span class="p">)</span></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seg</span><span class="p">[</span><span class="s">&#39;file&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">tokens</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">tokens</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;cmdline&#39;</span><span class="p">:</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seg</span><span class="p">[</span><span class="s">&#39;addr&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;0&#39;</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seg</span><span class="p">[</span><span class="s">&#39;flags&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;cmdline&#39;</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">input</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">&quot;^(0x[0-9a-fA-F]+)(?:,(ramdisk|ipl|entry|rpm))?$&quot;</span><span class="p">,</span> <span class="n">tokens</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span><span class="o">.</span><span class="n">groups</span><span class="p">()</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seg</span><span class="p">[</span><span class="s">&#39;addr&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">input</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seg</span><span class="p">[</span><span class="s">&#39;flags&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">input</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">segs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">seg</span><span class="p">)</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fatal</span><span class="p">(</span><span class="s">&quot;Incorrect format of input parameter: &quot;</span> <span class="o">+</span> <span class="n">arg</span><span class="p">)</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">segs</span></div><div class='line' id='LC91'><br/></div><div class='line' id='LC92'><span class="k">def</span> <span class="nf">write_elf_header</span><span class="p">(</span><span class="n">elf</span><span class="p">,</span> <span class="n">entry</span><span class="p">,</span> <span class="n">phnum</span><span class="p">):</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfhdr</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_ident&#39;</span><span class="p">:</span> <span class="s">&#39;</span><span class="se">\x7f</span><span class="s">ELF</span><span class="se">\x01\x01\x01\x61</span><span class="s">&#39;</span><span class="p">,</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_type&#39;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_machine&#39;</span><span class="p">:</span> <span class="mi">40</span><span class="p">,</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_version&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_entry&#39;</span><span class="p">:</span> <span class="nb">long</span><span class="p">(</span><span class="n">entry</span><span class="p">,</span> <span class="mi">16</span><span class="p">),</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_phoff&#39;</span><span class="p">:</span> <span class="mi">52</span><span class="p">,</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_shoff&#39;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_flags&#39;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_ehsize&#39;</span><span class="p">:</span> <span class="mi">52</span><span class="p">,</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_phentsize&#39;</span><span class="p">:</span> <span class="mi">32</span><span class="p">,</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_phnum&#39;</span><span class="p">:</span> <span class="n">phnum</span><span class="p">,</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_shentsize&#39;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_shnum&#39;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;e_shstrndx&#39;</span><span class="p">:</span> <span class="mi">0</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC109'><br/></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elf</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s">&#39;&lt;8s8xHHLLLLLHHHHHH&#39;</span><span class="p">,</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_ident&#39;</span><span class="p">],</span> <span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_type&#39;</span><span class="p">],</span> <span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_machine&#39;</span><span class="p">],</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_version&#39;</span><span class="p">],</span> <span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_entry&#39;</span><span class="p">],</span> <span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_phoff&#39;</span><span class="p">],</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_shoff&#39;</span><span class="p">],</span> <span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_flags&#39;</span><span class="p">],</span> <span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_ehsize&#39;</span><span class="p">],</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_phentsize&#39;</span><span class="p">],</span> <span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_phnum&#39;</span><span class="p">],</span> <span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_shentsize&#39;</span><span class="p">],</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_shnum&#39;</span><span class="p">],</span> <span class="n">elfhdr</span><span class="p">[</span><span class="s">&#39;e_shstrndx&#39;</span><span class="p">]))</span></div><div class='line' id='LC116'><br/></div><div class='line' id='LC117'><span class="k">def</span> <span class="nf">write_elf_phdr</span><span class="p">(</span><span class="n">elf</span><span class="p">,</span> <span class="n">seg</span><span class="p">):</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">type</span> <span class="o">=</span> <span class="n">PT_LOAD</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flags</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC120'><br/></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">seg</span><span class="p">[</span><span class="s">&#39;flags&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;ramdisk&#39;</span><span class="p">:</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flags</span> <span class="o">=</span> <span class="n">P_FLAGS_RAMDISK</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">seg</span><span class="p">[</span><span class="s">&#39;flags&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;ipl&#39;</span><span class="p">:</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flags</span> <span class="o">=</span> <span class="n">P_FLAGS_IPL</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">seg</span><span class="p">[</span><span class="s">&#39;flags&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;cmdline&#39;</span><span class="p">:</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flags</span> <span class="o">=</span> <span class="n">P_FLAGS_CMDLINE</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">type</span> <span class="o">=</span> <span class="n">PT_NOTE</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">seg</span><span class="p">[</span><span class="s">&#39;flags&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;rpm&#39;</span><span class="p">:</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flags</span> <span class="o">=</span> <span class="n">P_FLAGS_RPM</span></div><div class='line' id='LC130'><br/></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfphdr</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;p_type&#39;</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;p_offset&#39;</span><span class="p">:</span> <span class="n">seg</span><span class="p">[</span><span class="s">&#39;offset&#39;</span><span class="p">],</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;p_vaddr&#39;</span><span class="p">:</span> <span class="nb">long</span><span class="p">(</span><span class="n">seg</span><span class="p">[</span><span class="s">&#39;addr&#39;</span><span class="p">],</span> <span class="mi">16</span><span class="p">),</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;p_paddr&#39;</span><span class="p">:</span> <span class="nb">long</span><span class="p">(</span><span class="n">seg</span><span class="p">[</span><span class="s">&#39;addr&#39;</span><span class="p">],</span> <span class="mi">16</span><span class="p">),</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;p_filesz&#39;</span><span class="p">:</span> <span class="n">seg</span><span class="p">[</span><span class="s">&#39;size&#39;</span><span class="p">],</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;p_memsz&#39;</span><span class="p">:</span> <span class="n">seg</span><span class="p">[</span><span class="s">&#39;size&#39;</span><span class="p">],</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;p_flags&#39;</span><span class="p">:</span> <span class="n">flags</span><span class="p">,</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;p_align&#39;</span><span class="p">:</span> <span class="mi">0</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC141'><br/></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elf</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s">&#39;&lt;LLLLLLLL&#39;</span><span class="p">,</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfphdr</span><span class="p">[</span><span class="s">&#39;p_type&#39;</span><span class="p">],</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfphdr</span><span class="p">[</span><span class="s">&#39;p_offset&#39;</span><span class="p">],</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfphdr</span><span class="p">[</span><span class="s">&#39;p_vaddr&#39;</span><span class="p">],</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfphdr</span><span class="p">[</span><span class="s">&#39;p_paddr&#39;</span><span class="p">],</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfphdr</span><span class="p">[</span><span class="s">&#39;p_filesz&#39;</span><span class="p">],</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfphdr</span><span class="p">[</span><span class="s">&#39;p_memsz&#39;</span><span class="p">],</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfphdr</span><span class="p">[</span><span class="s">&#39;p_flags&#39;</span><span class="p">],</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elfphdr</span><span class="p">[</span><span class="s">&#39;p_align&#39;</span><span class="p">]))</span></div><div class='line' id='LC151'><br/></div><div class='line' id='LC152'><span class="k">def</span> <span class="nf">main</span><span class="p">(</span><span class="n">args</span><span class="p">):</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span> <span class="o">=</span> <span class="n">OptionParser</span><span class="p">(</span><span class="s">&quot;usage: %prog options&quot;</span><span class="p">)</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-o&quot;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&quot;outputfile&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;path to the output file&quot;</span><span class="p">)</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="n">opts</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span></div><div class='line' id='LC156'><br/></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">opts</span><span class="o">.</span><span class="n">outputfile</span><span class="p">:</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fatal</span><span class="p">(</span><span class="s">&quot;Missing -o on command line&quot;</span><span class="p">)</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fatal</span><span class="p">(</span><span class="s">&quot;Missing input files&quot;</span><span class="p">)</span></div><div class='line' id='LC161'><br/></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">offset</span> <span class="o">=</span> <span class="mi">4096</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">segments</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">seg</span> <span class="ow">in</span> <span class="n">parse_inputs</span><span class="p">(</span><span class="n">args</span><span class="p">):</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">size</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">getsize</span><span class="p">(</span><span class="n">seg</span><span class="p">[</span><span class="s">&#39;file&#39;</span><span class="p">])</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seg</span><span class="p">[</span><span class="s">&#39;offset&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">offset</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seg</span><span class="p">[</span><span class="s">&#39;size&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">size</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">segments</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">seg</span><span class="p">)</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">offset</span> <span class="o">+=</span> <span class="n">size</span></div><div class='line' id='LC170'><br/></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elf</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">opts</span><span class="o">.</span><span class="n">outputfile</span><span class="p">,</span> <span class="s">&#39;wb&#39;</span><span class="p">)</span></div><div class='line' id='LC172'><br/></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">write_elf_header</span><span class="p">(</span><span class="n">elf</span><span class="p">,</span> <span class="n">segments</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s">&#39;addr&#39;</span><span class="p">],</span> <span class="nb">len</span><span class="p">(</span><span class="n">segments</span><span class="p">))</span></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">seg</span> <span class="ow">in</span> <span class="n">segments</span><span class="p">:</span></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">write_elf_phdr</span><span class="p">(</span><span class="n">elf</span><span class="p">,</span> <span class="n">seg</span><span class="p">)</span></div><div class='line' id='LC176'><br/></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">seg</span> <span class="ow">in</span> <span class="n">segments</span><span class="p">:</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elf</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="n">seg</span><span class="p">[</span><span class="s">&#39;offset&#39;</span><span class="p">])</span></div><div class='line' id='LC179'><br/></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">seg</span><span class="p">[</span><span class="s">&#39;file&#39;</span><span class="p">],</span> <span class="s">&#39;rb&#39;</span><span class="p">)</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elf</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC184'><br/></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elf</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC186'><br/></div><div class='line' id='LC187'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">main</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:])</span></div><div class='line' id='LC189'><br/></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>
      </div>

      <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
      <div id="jump-to-line" style="display:none">
        <h2>Jump to Line</h2>
        <form accept-charset="UTF-8" class="js-jump-to-line-form">
          <input class="textfield js-jump-to-line-field" type="text">
          <div class="full-button">
            <button type="submit" class="classy">
              Go
            </button>
          </div>
        </form>
      </div>

    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1347543529" height="64" width="64">
</div>


        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2012 <span title="0.05882s from fe13.rs.github.com">GitHub</span> Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-icon mega-icon-invertocat"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus command bar</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style='display:none'>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Expand URL to its canonical form</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last js-hidden-pane" style='display:none'>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
        <dd>Submit comment</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> shift p</dt>
        <dd>Preview comment</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle selection</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
          <dd>Submit comment</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> shift p</dt>
          <dd>Preview comment</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>

    <h3>Issues Dashboard</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div class="js-hidden-pane" >
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first js-hidden-pane" >
        <h3>Source Code Browsing</h3>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>w</dt>
          <dd>Switch branch/tag</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Expand URL to its canonical form</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first">
        <h3>Browsing Commits</h3>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
          <dd>Submit comment</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>escape</dt>
          <dd>Close form</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>p</dt>
          <dd>Parent commit</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o</dt>
          <dd>Other parent commit</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>
    <h3>Notifications</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open notification</dd>
        </dl>
      </div><!-- /.column.first -->

      <div class="column second">
        <dl class="keyboard-mappings">
          <dt>e <em>or</em> shift i <em>or</em> y</dt>
          <dd>Mark as read</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift m</dt>
          <dd>Mute thread</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

</div>

    <div id="markdown-help" class="instapaper_ignore readability-extra">
  <h2>Markdown Cheat Sheet</h2>

  <div class="cheatsheet-content">

  <div class="mod">
    <div class="col">
      <h3>Format Text</h3>
      <p>Headers</p>
      <pre>
# This is an &lt;h1&gt; tag
## This is an &lt;h2&gt; tag
###### This is an &lt;h6&gt; tag</pre>
     <p>Text styles</p>
     <pre>
*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__

*You **can** combine them*
</pre>
    </div>
    <div class="col">
      <h3>Lists</h3>
      <p>Unordered</p>
      <pre>
* Item 1
* Item 2
  * Item 2a
  * Item 2b</pre>
     <p>Ordered</p>
     <pre>
1. Item 1
2. Item 2
3. Item 3
   * Item 3a
   * Item 3b</pre>
    </div>
    <div class="col">
      <h3>Miscellaneous</h3>
      <p>Images</p>
      <pre>
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
</pre>
     <p>Links</p>
     <pre>
http://github.com - automatic!
[GitHub](http://github.com)</pre>
<p>Blockquotes</p>
     <pre>
As Kanye West said:

> We're living the future so
> the present is our past.
</pre>
    </div>
  </div>
  <div class="rule"></div>

  <h3>Code Examples in Markdown</h3>
  <div class="col">
      <p>Syntax highlighting with <a href="http://github.github.com/github-flavored-markdown/" title="GitHub Flavored Markdown" target="_blank">GFM</a></p>
      <pre>
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```</pre>
    </div>
    <div class="col">
      <p>Or, indent your code 4 spaces</p>
      <pre>
Here is a Python code example
without syntax highlighting:

    def foo:
      if not bar:
        return true</pre>
    </div>
    <div class="col">
      <p>Inline code for comments</p>
      <pre>
I think you should use an
`&lt;addr&gt;` element here instead.</pre>
    </div>
  </div>

  </div>
</div>


    <div id="ajax-error-message" class="flash flash-error">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="mini-icon mini-icon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.06004' data-host='fe13'></span>
    
  </body>
</html>


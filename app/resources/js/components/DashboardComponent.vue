<template>
    <div class="container" >
  <div class="left-side" :class="{'active' : leftSide}">
    <div class="left-side-button" @click="leftSide = !leftSide">
      <svg viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      <svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
  <path d="M19 12H5M12 19l-7-7 7-7"/>
</svg>
    </div>
    <div class="logo">Onion</div>
    <SideMenuComponent></SideMenuComponent>
    
    <a href="https://twitter.com/HungTra51048517" class="follow-me" target="_blank">
      <span class="follow-text">
        <svg viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>
        Follow me on Twitter
     </span>
      <span class="developer">
        <img src="https://avatars0.githubusercontent.com/u/39208974?s=460&u=48aef927b291ab830fea070bd6b9b5acd9a67b80&v=4" />
        Polowis - @hungtran
      </span>
    </a>
  </div>
  <div class="main">
    <div class="search-bar">
      <input type="text" placeholder="Search" />
      <button class="right-side-button" @click="rightSide = !rightSide">
         <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
      </button>
    </div>
    <div class="main-container">
      <div class="profile">
        <div class="profile-avatar">
          <img src="https://avatars0.githubusercontent.com/u/39208974?s=460&u=48aef927b291ab830fea070bd6b9b5acd9a67b80&v=4" alt="" class="profile-img">
          <div class="profile-name">{{ user.name }}</div>
        </div>
        <img src="https://images.unsplash.com/photo-1508247967583-7d982ea01526?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80" alt="" class="profile-cover">
        <div class="profile-menu">
          <a class="profile-menu-link active">Timeline</a>
          <a class="profile-menu-link">About</a>
          <a class="profile-menu-link">Friends</a>
          <a class="profile-menu-link">Photos</a>
          <a class="profile-menu-link">More</a>
        </div>
      </div>
      <div class="timeline">
        <div class="timeline-left">
          <div class="intro" style="background-color: #151728;">
            <div class="intro-title">
              Introduction
              <button class="intro-menu"></button>
            </div>
            <div class="info">
              <div class="info-item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 503.889 503.889" fill="currentColor">
                  <path d="M453.727 114.266H345.151V70.515c0-20.832-16.948-37.779-37.78-37.779H196.517c-20.832 0-37.78 16.947-37.78 37.779v43.751H50.162C22.502 114.266 0 136.769 0 164.428v256.563c0 27.659 22.502 50.161 50.162 50.161h403.565c27.659 0 50.162-22.502 50.162-50.161V164.428c0-27.659-22.503-50.162-50.162-50.162zm-262.99-43.751a5.786 5.786 0 015.78-5.779h110.854a5.786 5.786 0 015.78 5.779v43.751H190.737zM32 164.428c0-10.015 8.147-18.162 18.162-18.162h403.565c10.014 0 18.162 8.147 18.162 18.162v23.681c0 22.212-14.894 42.061-36.22 48.27l-167.345 48.723a58.482 58.482 0 01-32.76 0L68.22 236.378C46.894 230.169 32 210.321 32 188.109zm421.727 274.725H50.162c-10.014 0-18.162-8.147-18.162-18.161V253.258c8.063 6.232 17.254 10.927 27.274 13.845 184.859 53.822 175.358 52.341 192.67 52.341 17.541 0 7.595 1.544 192.67-52.341 10.021-2.918 19.212-7.613 27.274-13.845v167.733c.001 10.014-8.147 18.162-18.161 18.162z" /></svg>
                Product Designer at <a href="#">Bravebist</a>
              </div>
              <div class="info-item">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
                  <path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z" />
                  <path d="M9 22V12h6v10" />
                </svg>
                Live in <a href="#">Hanoi, Vietnam</a>
              </div>
              <div class="info-item">
                <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" fill="currentColor">
                  <path d="M437 75C388.7 26.6 324.4 0 256 0S123.3 26.6 75 75C26.6 123.3 0 187.6 0 256s26.6 132.7 75 181c48.3 48.4 112.6 75 181 75s132.7-26.6 181-75c48.4-48.3 75-112.6 75-181s-26.6-132.7-75-181zM252.4 481.9c-52-.9-103.7-19.5-145.2-55.8L256 277.2l21.7 21.8a165.9 165.9 0 00-35.7 87c-3.5 30.5 0 63.3 10.4 95.9zM299 320.3l105.7 105.8a224.8 224.8 0 01-121.3 54.1C262 419.5 268 360.3 299 320.3zm21.2-21.2c40-31 99.2-37 160-15.6A224.8 224.8 0 01426 404.8zM482 252.4a231.7 231.7 0 00-96-10.4 165.9 165.9 0 00-87 35.7L277.3 256l148.9-148.8c36.3 41.5 55 93.2 55.8 145.2zm-290.2-39.5c-40 31-99.2 37-160 15.6A224.8 224.8 0 0186 107.2zm-84.5-127a224.8 224.8 0 01121.3-54.1C250 92.5 244 151.7 213 191.7zM270 126c3.5-30.5 0-63.3-10.4-95.9 52 .9 103.7 19.5 145.2 55.8L256 234.8 234.3 213a165.9 165.9 0 0035.7-87zM30 259.6a242 242 0 0072.7 11.7c7.8 0 15.6-.5 23.2-1.3a165.9 165.9 0 0087-35.7l21.8 21.7L85.9 404.8a225.3 225.3 0 01-55.8-145.2z" /></svg>
                Username <a href="#">{{user.name}}</a>
              </div>
            </div>
          </div>
          <!--
          <div class="event box">
            <div class="event-wrapper">
              <img src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80" class="event-img" />
              <div class="event-date">
                <div class="event-month">Jan</div>
                <div class="event-day">01</div>
              </div>
              <div class="event-title">Winter Wonderland</div>
              <div class="event-subtitle">01st Jan, 2019 07:00AM</div>
            </div>
          </div>-->
          <div class="pages" style="background-color: #151728;">
            <div class="intro-title">
              Your pages
              <button class="intro-menu"></button>
            </div>
            <div class="user">
              <img src="https://images.unsplash.com/photo-1549068106-b024baf5062d?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&ixid=eyJhcHBfaWQiOjE3Nzg0f" alt="" class="user-img">
              <div class="username">Chandelio</div>
            </div>
            <div class="user">
              <img src="https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&s=d5849d81af587a09dbcf3f11f6fa122f" alt="" class="user-img">
              <div class="username">Janet Jolie</div>
            </div>
            <div class="user">
              <img src="https://images.unsplash.com/photo-1546539782-6fc531453083?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&ixid=eyJhcHBfaWQiOjE3Nzg0fQ" alt="" class="user-img">
              <div class="username">Patrick Watsons</div>
            </div>
          </div>
        </div>
        <div class="timeline-right">
          <!----
          Status stage
          -->
          <div class="status" style="background-color: #151728;" v-if="this.stage == 'status'">
            <div class="status-menu">
              <a class="status-menu-item active" href="#" @click.prevent="switchStatusStage()">Status</a>
              <a class="status-menu-item" href="#" @click.prevent="switchPhotoStage()">Photos</a>
              <a class="status-menu-item" href="#">Videos</a>
            </div>
            <div class="status-main" >
              <img src="https://avatars0.githubusercontent.com/u/39208974?s=460&u=48aef927b291ab830fea070bd6b9b5acd9a67b80&v=4" class="status-img">
              <textarea class="status-textarea" v-model="status" placeholder="Write something..."></textarea>
            </div>
            <div class="status-actions">
              <a href="#" class="status-action">
                <svg viewBox="-42 0 512 512" xmlns="http://www.w3.org/2000/svg">
                  <path d="M333.7 123.3c0 33.9-12.2 63.2-36.2 87.2-24 24-53.3 36.1-87.1 36.1h-.1c-33.9 0-63.2-12.1-87.1-36.1-24-24-36.2-53.3-36.2-87.2 0-33.9 12.2-63.2 36.2-87.2 24-24 53.2-36 87-36.1h.2c33.8 0 63.2 12.2 87.1 36.1 24 24 36.2 53.3 36.2 87.2zm0 0" fill="#ffbb85" />
                  <path d="M427.2 424c0 26.7-8.5 48.3-25.3 64.3-16.5 15.7-38.4 23.7-65 23.7H90.2c-26.6 0-48.5-8-65-23.7C8.5 472.3 0 450.7 0 423.9c0-10.2.3-20.4 1-30.2a302.7 302.7 0 0112.1-64.9c3.3-10.3 7.8-20.5 13.4-30.3 5.8-10.2 12.5-19 20.1-26.3a89 89 0 0129-18.2c11.2-4.4 23.7-6.7 37-6.7 5.2 0 10.3 2.2 20 8.5l21 13.5c6.6 4.3 15.7 8.3 27 11.9a107.7 107.7 0 0033 5.3c11 0 22-1.8 33-5.3 11.2-3.6 20.3-7.6 27-12l21-13.4c9.7-6.3 14.7-8.5 20-8.5 13.3 0 25.7 2.3 37 6.7a89 89 0 0128.9 18.2c7.6 7.3 14.4 16.1 20.2 26.3 5.5 9.8 10 20 13.3 30.3a305.5 305.5 0 0112.1 64.9c.7 9.8 1 20 1 30.2zm0 0" fill="#6aa9ff" />
                  <path d="M210.4 246.6h-.1V0c34 0 63.3 12.2 87.2 36.1 24 24 36.2 53.3 36.2 87.2 0 33.9-12.2 63.2-36.2 87.2-24 24-53.3 36.1-87.1 36.1zm0 0" fill="#f5a86c" />
                  <path d="M427.2 424c0 26.7-8.5 48.3-25.3 64.3-16.5 15.7-38.4 23.7-65 23.7H210.2V286.5h3.3c11 0 22-1.8 33-5.3 11.2-3.6 20.3-7.6 27-12l21-13.4c9.7-6.3 14.7-8.5 20-8.5 13.3 0 25.7 2.3 37 6.7a89 89 0 0128.9 18.2c7.6 7.3 14.4 16.1 20.2 26.3 5.5 9.8 10 20 13.3 30.3a305.5 305.5 0 0112.1 64.9c.7 9.8 1 20 1 30.2zm0 0" fill="#2682ff" />
                </svg>
                People
              </a>
              <a href="#" class="status-action">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                  <path d="M87.084 192c-.456-5.272-.688-10.6-.688-16C86.404 78.8 162.34 0 256.004 0s169.6 78.8 169.6 176c0 5.392-.232 10.728-.688 16h.688c0 96.184-169.6 320-169.6 320s-169.6-223.288-169.6-320h.68zm168.92 32c36.392 1.024 66.744-27.608 67.84-64-1.096-36.392-31.448-65.024-67.84-64-36.392-1.024-66.744 27.608-67.84 64 1.096 36.392 31.448 65.024 67.84 64z" fill="#e21b1b" />
                </svg>
                Check in
              </a>
              <a href="#" class="status-action">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                  <circle cx="256" cy="256" r="256" fill="#ffca28" />
                  <g fill="#6d4c41">
                    <path d="M399.68 208.32c-8.832 0-16-7.168-16-16 0-17.632-14.336-32-32-32s-32 14.368-32 32c0 8.832-7.168 16-16 16s-16-7.168-16-16c0-35.296 28.704-64 64-64s64 28.704 64 64c0 8.864-7.168 16-16 16zM207.68 208.32c-8.832 0-16-7.168-16-16 0-17.632-14.368-32-32-32s-32 14.368-32 32c0 8.832-7.168 16-16 16s-16-7.168-16-16c0-35.296 28.704-64 64-64s64 28.704 64 64c0 8.864-7.168 16-16 16z" />
                  </g>
                  <path d="M437.696 294.688c-3.04-4-7.744-6.368-12.736-6.368H86.4c-5.024 0-9.728 2.336-12.736 6.336-3.072 4.032-4.032 9.184-2.688 14.016C94.112 390.88 170.08 448.32 255.648 448.32s161.536-57.44 184.672-139.648c1.376-4.832.416-9.984-2.624-13.984z" fill="#fafafa" />
                </svg>
                Mood
              </a>
              <button class="status-share" @click.prevent="createStatus()">Share</button>
            </div>
          </div>
          <!--


              Photo stage


            -->
          <div class="status" style="background-color: #151728;" v-if="this.stage == 'photo'">
            <div class="status-menu">
              <a class="status-menu-item" href="#" @click.prevent="switchStatusStage()">Status</a>
              <a class="status-menu-item active" @click.prevent="switchPhotoStage()" href="#">Photos</a>
              <a class="status-menu-item" href="#">Videos</a>
            </div>
            <div class="status-main" >
              <img src="https://avatars0.githubusercontent.com/u/39208974?s=460&u=48aef927b291ab830fea070bd6b9b5acd9a67b80&v=4" class="status-img">
              <textarea class="status-textarea" v-model="status" placeholder="Write something..."></textarea>
            </div>
            <div class="status-actions">
              <i class="fa fa-upload" aria-hidden="true">
              <a href="#" class="status-action">
                People
                
              </a>
              </i>
              <label>
                  <input type="file" id="file" ref="file" v-on:change="handlePhotoUpload()"/>
                </label>
              <button class="status-share" @click.prevent="createPhoto()">Share</button>
            </div>
          </div>

            <!--
              Timeline
              -->
          <div class="album" style="background-color: #151728;" v-for="item in task.slice().reverse()" :key="item.id">
            <div class="status-main">
              <img src="https://avatars0.githubusercontent.com/u/39208974?s=460&u=48aef927b291ab830fea070bd6b9b5acd9a67b80&v=4" class="status-img"/>
              <div class="album-detail">
                <div class="album-title"><strong>{{user.name}}</strong> posted a new <span v-if="item.photo == null">status</span><span v-else>photo</span> on their timeline</div>
                <div class="album-date">6 hours ago</div>
              </div>
              <button class="intro-menu"></button>
            </div>
            <div class="album-content">{{item.content}}
              <div class="album-photos">
                <img v-if="item.photo != null" :src="'/static/uploads/' + item.photo" alt="" class="album-photo"/>
              </div>
          </div>
          <div class="album-actions">
              <a href="#" class="album-action">
                <svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
                  <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z" />
                </svg>
                87
              </a>
              <a href="#" class="album-action">
                <svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1" viewBox="0 0 24 24">
                  <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" />
                </svg>
                20
              </a>
              <a href="#" class="album-action">
                <svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1" viewBox="0 0 24 24">
                  <path d="M17 1l4 4-4 4" />
                  <path d="M3 11V9a4 4 0 014-4h14M7 23l-4-4 4-4" />
                  <path d="M21 13v2a4 4 0 01-4 4H3" />
                </svg>
                13
              </a>
            </div>
          </div>
          <div class="album " style="background-color: #151728;">
            <div class="status-main">
              <img src="https://avatars0.githubusercontent.com/u/39208974?s=460&u=48aef927b291ab830fea070bd6b9b5acd9a67b80&v=4" class="status-img" />
              <div class="album-detail">
                <div class="album-title"><strong>{{user.name}}</strong> create new <span>album</span></div>
                <div class="album-date">6 hours ago</div>
              </div>
              <button class="intro-menu"></button>
            </div>
            <div class="album-content">When the bass drops, so do my problems.
              <div class="album-photos">
                <img src="https://images.unsplash.com/photo-1508179719682-dbc62681c355?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2378&q=80" alt="" class="album-photo" />
              </div>
            </div>
            <div class="album-actions">
              <a href="#" class="album-action">
                <svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
                  <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z" />
                </svg>
                87
              </a>
              <a href="#" class="album-action">
                <svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1" viewBox="0 0 24 24">
                  <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" />
                </svg>
                20
              </a>
              <a href="#" class="album-action">
                <svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1" viewBox="0 0 24 24">
                  <path d="M17 1l4 4-4 4" />
                  <path d="M3 11V9a4 4 0 014-4h14M7 23l-4-4 4-4" />
                  <path d="M21 13v2a4 4 0 01-4 4H3" />
                </svg>
                13
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="right-side" :class="{ 'active': rightSide }">
    <div class="account">
      <button class="account-button">
        <svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1" viewBox="0 0 24 24">
          <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
          <path d="M22 6l-10 7L2 6" />
        </svg>
      </button>
      <button class="account-button">
        <svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1" viewBox="0 0 24 24">
          <path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9M13.73 21a2 2 0 01-3.46 0" />
        </svg>
      </button>
      <span class="account-user">{{ user.name }}
        <img src="https://avatars0.githubusercontent.com/u/39208974?s=460&u=48aef927b291ab830fea070bd6b9b5acd9a67b80&v=4" alt="" class="account-profile">
        <span>▼</span>
      </span>
    </div>
    <div class="side-wrapper stories">
      <div class="side-title">STORIES</div>
      <div class="user">
        <img src="https://pbs.twimg.com/profile_images/1102351320567164931/ZCkJgJIH.png" alt="" class="user-img">
        <div class="username">Lisandro Matos
          <div class="album-date">12 hours ago</div>
        </div>
      </div>
      <div class="user">
        <img src="https://pbs.twimg.com/profile_images/1153966095444992000/1lpIyHaQ.jpg" alt="" class="user-img">
        <div class="username">Gvozden Boskovsky
          <div class="album-date">29 minutes ago</div>
        </div>
      </div>
      <div class="user">
        <img src="https://pbs.twimg.com/profile_images/1157046181698011136/xZ4wg2Xj.jpg" alt="" class="user-img">
        <div class="username">Hnek Fortuin
          <div class="album-date">3 hours ago</div>
        </div>
      </div>
      <div class="user">
        <img src="https://pbs.twimg.com/profile_images/1108443816565059590/Te-0H20q.png" alt="" class="user-img">
        <div class="username">Lubomir Dvorak
          <div class="album-date">18 hours ago</div>
        </div>
      </div>
    </div>
    <div class="side-wrapper contacts">
      <div class="side-title">CONTACTS</div>
      <div class="user">
        <img src="https://randomuser.me/api/portraits/men/1.jpg" class="user-img">
        <div class="username">Andrei Mashrin
          <div class="user-status"></div>
        </div>
      </div>
      <div class="user">
        <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&s=046c29138c1335ef8edee7daf521ba50" class="user-img">
        <div class="username">Aryn Jacobssen
          <div class="user-status offline"></div>
        </div>
      </div>
      <div class="user">
        <img src="https://tinyfac.es/data/avatars/7D3FA6C0-83C8-4834-B432-6C65ED4FD4C3-500w.jpeg" class="user-img">
        <div class="username">Carole Landu
          <div class="user-status offline"></div>
        </div>
      </div>
      <div class="user">
        <img src="https://images.pexels.com/photos/598745/pexels-photo-598745.jpeg?h=350&auto=compress&cs=tinysrgb" class="user-img">
        <div class="username">Chineze Afa
          <div class="user-status"></div>
        </div>
      </div>
      <div class="user">
        <img src="https://pbs.twimg.com/profile_images/2452384114/noplz47r59v1uxvyg8ku.png" class="user-img">
        <div class="username">Mok Kwang
          <div class="user-status"></div>
        </div>
      </div>
      <div class="user">
        <img src="https://randomuser.me/api/portraits/women/63.jpg" class="user-img">
        <div class="username">Naomi Yepes
          <div class="user-status"></div>
        </div>
      </div>
      <div class="user">
        <img src="https://images.unsplash.com/photo-1476493279419-b785d41e38d8?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&s=61eaea85f1aa3d065400179c78163f15" class="user-img">
        <div class="username">Shaamikh Ale
          <div class="user-status"></div>
        </div>
      </div>
      <div class="user">
        <img src="https://m.media-amazon.com/images/M/MV5BMjI4NDcyNjQxNl5BMl5BanBnXkFtZTgwMzI4OTM3NjM@._V1_UY256_CR13,0,172,256_AL_.jpg" class="user-img">
        <div class="username">Sofia Alcocer
          <div class="user-status idle"></div>
        </div>
      </div>
      <div class="user">
        <img src="https://images.unsplash.com/photo-1509380836717-c4320ccf1a6f?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&s=e01c8c45a063daaf6d6e571a32bd6c90" class="user-img">
        <div class="username">Wen Yahui
          <div class="user-status"></div>
        </div>
      </div>
      <div class="user">
        <img src="https://pbs.twimg.com/profile_images/737221709267374081/sdwta9Oh.jpg" alt="" class="user-img">
        <div class="username">Leslee Moss
          <div class="user-status idle"></div>
        </div>
      </div>
    </div>
    <div class="search-bar right-search">
      <input type="text" placeholder="Search" />
      <div class="search-bar-svgs">
        <svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1" viewBox="0 0 24 24">
          <circle cx="12" cy="12" r="3"/>
          <path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-2 2 2 2 0 01-2-2v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83 0 2 2 0 010-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 01-2-2 2 2 0 012-2h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 010-2.83 2 2 0 012.83 0l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 012-2 2 2 0 012 2v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 0 2 2 0 010 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 012 2 2 2 0 01-2 2h-.09a1.65 1.65 0 00-1.51 1z"/>
        </svg>
        <svg fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 469.34 469.34">
          <path d="M456.84 76.17l-64-64.06c-16.13-16.13-44.18-16.17-60.37.04L45.77 301.67a10.73 10.73 0 00-2.7 4.59L.41 455.73a10.68 10.68 0 0013.19 13.2l149.33-42.7c1.73-.5 3.3-1.42 4.58-2.7l289.33-286.98c8.06-8.07 12.5-18.78 12.5-30.19s-4.44-22.12-12.5-30.2zM285.99 89.74L325.25 129l-205 205-14.7-29.44a10.67 10.67 0 00-9.55-5.9H78.92L286 89.75zM26.2 443.14l13.9-48.64 34.74 34.74-48.64 13.9zm123.14-35.18L98.3 422.54l-51.5-51.5L61.38 320H89.4l18.38 36.77a10.67 10.67 0 004.77 4.77l36.78 18.39v28.03zm21.33-17.54v-17.09c0-4.04-2.28-7.72-5.9-9.54l-29.43-14.7 205-205 39.26 39.26-208.93 207.07zm271.11-268.7l-47.03 46.61L301 74.6l46.59-47c8.06-8.07 22.1-8.07 30.16 0l64 64c4.03 4.03 6.25 9.38 6.25 15.08s-2.22 11.05-6.22 15.05z" /></svg>
        <svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
      <path d="M12 5v14M5 12h14"/>
    </svg>
      </div>
    </div>
  </div>
  <div class="overlay" @click="rightSide = false; leftSide = false" :class="{ 'active': rightSide || leftSide }"></div>
</div>
</template>
<script>
import SideMenuComponent from './SideMenuComponent'
export default {
    props: ['user'],
    components: {
        SideMenuComponent
    },
      
    data(){
        return {
            rightSide: true,
            leftSide: true,
            status: "",
            task: [],
            stage: "status",
            file: ""
        }
    },
    methods: {
      createStatus(){
        if(this.status.length < 1) return;
        axios.post('/api/status/create', {content: this.status}).then(response => {
          if(response.data.message == 'Success'){
            this.task.push({
              id: response.data.id,
              content: response.data.content,
              photo: response.data.photo
            })
          }
          
        })
      },

      deleteStatus(){

      },

      createPhoto(){
        if(this.status.length < 1) return;
        let formData = new FormData()
        formData.append('file', this.file)
        formData.append('content', this.status)
        axios.post('/api/photo/create', 
               
          formData, 
          { 
            headers: {
            'Content-Type': 'multipart/form-data'
            }
          }
        ).then(response => {
          if(response.data.message == 'Success') {
            this.task.push({
              id: response.data.id,
              content: response.data.content,
              photo: response.data.photo
            })
          }
        })
      },

      fetchStatus() {
        axios.get('/api/status/'+ this.user.user_id).then(response => {
            this.task = response.data;
        });
      },

      switchStatusStage(){
        this.stage = "status"
      },

      switchPhotoStage(){
        this.stage = "photo"
      },

      handlePhotoUpload(){
        this.file = this.$refs.file.files[0];
      }


    },
     beforeMount(){
      this.fetchStatus()
    }

}
</script>


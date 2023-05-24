// 리액트 기본 설정
import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";

// 전역 변수 중 일부를 영속적으로 로컬 스토리지에 저장
import { recoilPersist } from "recoil-persist";

// 화면 이동
import {
  BrowserRouter as Router,
  Routes,
  Route,
  NavLink,
  Navigate,
  useParams,
  useNavigate,
} from "react-router-dom";

// 통신 API
import axios from "axios";

// 클래스이름 동적 변경에 편리함
import classNames from "classnames";

import AccountLoginPage from "./routes/AccountLoginPage";
import Header from "./components/Header";
import HomeMainPage from "./routes/HomeMainPage";

// 부트스트랩
import "bootstrap/dist/css/bootstrap.min.css";

// css
import styles from "./css/App.module.css";

const persistAtom = recoilPersist();
const axiosInstance = axios.create();

function App() {
  return (
    <div>
      <Router>
        <Header />
        <Routes>
          <Route path="/account/login" element={<AccountLoginPage />} />
          <Route path="/home/main" element={<HomeMainPage />} />
          <Route path="*" element={<Navigate to="/home/main" />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;

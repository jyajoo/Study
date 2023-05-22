// 리액트 기본 설정
import React, { useState, useEffect } from "react";
import { ReactDOM } from "react";

// 상태 관리, 전역 변수 관리, 컴포넌트간 데이터 공유
import {
  RecoilRoot,
  atom,
  useRecoilState,
  useRecoilValue,
  selector,
} from "recoil";

// 전역 변수 중 일부를 영속적으로 로컬 스토리지에 저장
import { recoilPersist } from "recoil-persist";

// 화면 이동
import {
  HashRouter as Router,
  Routes,
  Route,
  NavLink,
  Navigate,
  useParams,
  useNavigate,
} from "react-router-dom";

// useEffect 없이 API 통신이 가능하도록
import { QueryClient, QueryClientProvider, useQuery } from "react-query";

// 통신 API
import axios from "axios";

// 클래스이름 동적 변경에 편리함
import classNames from "classnames";

const persistAtom = recoilPersist();
const queryClient = new QueryClient();
const axiosInstance = axios.create();

function App() {
  return <div>모든 것 로딩 완료</div>;
}

ReactDOM.render(
  <React.StrictMode>
    <RecoilRoot>
      <QueryClientProvider client={queryClient}>
        <App />
      </QueryClientProvider>
    </RecoilRoot>
  </React.StrictMode>,
  document.getElementById("root")
);
export default App;

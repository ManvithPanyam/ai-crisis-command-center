import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyCFf12ejKktTCRs0_r2cpvhPgujY7ISzL4",
  authDomain: "https://ai-crisis-command-center-ee158.firebaseapp.com/",
  projectId: "ai-crisis-command-center-ee158",
  storageBucket: "https://ai-crisis-command-center-ee158.firebasestorage.app/",
  messagingSenderId: "89585569762",
  appId: "1:89585569762:web:d9da6cbc888c507fcd33bb"
};

const app = initializeApp(firebaseConfig);

export default app;
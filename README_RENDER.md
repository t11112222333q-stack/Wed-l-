# Deploy lên Render.com

## Cách 1: Deploy từ GitHub (Khuyên dùng)
1. Tạo repo GitHub, upload 3 file này
2. Vào Render → New Web Service → Connect GitHub repo
3. Render tự động nhận `render.yaml`
4. Bấm Deploy

## Cách 2: Deploy bằng Render CLI
```bash
pip install render
render deploy
```

## Truy cập
Sau khi deploy xong, Render sẽ cấp URL dạng:
https://web-leak-scanner-xxxx.onrender.com

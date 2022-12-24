function getJadwalSholat() {
    fetch('https://api.banghasan.com/sholat/format/json/jadwal/kota/703/tanggal/2022-12-04')
    .then(response => console.log(response));
}

getJadwalSholat();
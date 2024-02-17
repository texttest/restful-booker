var Booking = require('../models/booking'),
    creator = require('../helpers/bookingcreator');

async function deleteAllBookings() {
    return new Promise((resolve, reject) => {
        Booking.deleteAll((err) => {
            if (err) reject(err);
            else resolve();
        });
    });
}

function createBookingAsync(bookingData) {
    return new Promise((resolve, reject) => {
        Booking.create(bookingData, function(err, result) {
            if (err) reject(err);
            else resolve(result);
        });
    });
}

const initializeSeedData = async function() {
    return new Promise(async (resolve, reject) => {
        try {
            try {
                await deleteAllBookings();
                console.log("All bookings deleted successfully.");
            } catch (error) {
                console.error("Failed to delete bookings:", error);
            }

            const totalBookings = 10;

            for (let count = 0; count < totalBookings; count++) {
                var newBooking = creator.createBooking();
                await createBookingAsync(newBooking);
                console.log(`Created booking ${count + 1}`);
            }

            console.log("Seeded database with generated bookings");
            resolve(); // Explicitly resolve the Promise
        } catch (err) {
            console.error("Error seeding database:", err);
            reject(err); // Explicitly reject the Promise
        }
    });
};

module.exports = initializeSeedData;

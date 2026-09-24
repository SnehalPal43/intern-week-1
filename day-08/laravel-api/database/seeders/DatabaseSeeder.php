<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Facility;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run(): void
    {
        Facility::create([
            'name' => 'Central Hospital',
            'location' => 'New York'
        ]);

        Facility::create([
            'name' => 'North Wing Inspection Center',
            'location' => 'Chicago'
        ]);
    }
}

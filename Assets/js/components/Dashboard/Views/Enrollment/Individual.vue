<template>
  <form>

    <fieldset>
      <legend>Personal Information</legend>
      <div class="form-row">
        <div class="form-group col">
          <label for="surname">Surname</label>
          <input type="text" class="form-control" id="surname" placeholder="Surname"
            v-model="taxPayer.surname" required>
        </div>
        <div class="form-group col">
          <label for="first_name">First Name</label>
          <input type="text" class="form-control" id="first_name" placeholder="First Name"
            v-model="taxPayer.first_name" required>
        </div>
        <div class="form-group col">
          <label for="other_name">Last Name</label>
          <input type="text" class="form-control" id="other_name" placeholder="Other Name"
            v-model="taxPayer.other_name" required>
        </div>
      </div>

      <div class="form-row">
        <div class="form-group col">
          <label for="dob">Birth Date</label>
          <input type="date" class="form-control" id="dob" placeholder="Birth Date"
            v-model="taxPayer.dob" required>
        </div>
        <div class="form-group col">
          <label for="gender">Gender</label>
          <select class="form-control" id="gender" placeholder="Gender"
            v-model="taxPayer.gender" required>
            <option v-for="gender in genderChoices" :key="gender"
              :value="gender">{{ gender }}</option>
          </select>
        </div>
        <div class="form-group col">
          <label for="marital_status">Marital Status</label>
          <select class="form-control" id="marital_status" placeholder="Marital Status"
            v-model="taxPayer.marital_status" required>
            <option v-for="marital_status in maritalStatusChoices" :key="marital_status"
              :value="marital_status">{{ marital_status }}</option>
          </select>
        </div>
      </div>

      <div class="form-row">
        <div class="form-group col">
          <label for="nationality">Nationality</label>
          <select class="form-control" id="nationality" placeholder="Nationality"
            v-model="taxPayer.nationality" required>
            <option v-for="nationality in countries" :key="nationality" :value="nationality">
              {{ nationality }}
            </option>
          </select>
        </div>
        <div class="form-group col">
          <label for="state_of_origin">State of Origin</label>
          <input type="text" class="form-control" id="state_of_origin" placeholder="State of Origin"
            v-model="taxPayer.state_of_origin" required>
        </div>
        <div class="form-group col">
          <label for="lga_of_origin">LGA of Origin</label>
          <input type="text" class="form-control" id="lga_of_origin" placeholder="Local Government Area"
            v-model="taxPayer.lga_of_origin" required>
        </div>
      </div>

      <div class="form-row">
        <div class="form-group col">
          <label for="occupation">Occupation</label>
          <input type="text" class="form-control" id="occupation" placeholder="Occupation"
            v-model="taxPayer.occupation" required>
        </div>
        <div class="form-group col">
          <label for="employment_status">Employment Status</label>
          <select class="form-control" id="employment_status" placeholder="Employment Status"
            v-model="taxPayer.employment_status" required>
            <option v-for="employment_status in employmentStatusChoices" :key="employment_status"
              :value="employment_status">
              {{ employment_status }}
            </option>
          </select>
        </div>
        <div class="form-group col">
          <label for="tax_payer_company">Company Name</label>
          <input type="text" class="form-control" id="tax_payer_company" placeholder="Company Name"
            v-model="taxPayer.tax_payer_company" required>
        </div>
      </div>
    </fieldset>

    <fieldset>
      <legend>Contact Information</legend>
      <div class="form-row">
        <div class="form-group col-4">
          <label for="house_no">House Number</label>
          <input type="text" class="form-control" id="house_no" placeholder="House Number"
            v-model="taxPayer.residential_address.house_no" required>
        </div>
        <form-group class="form-group col-8">
          <label for="street">Street</label>
          <input type="text" class="form-control" id="street" placeholder="Street"
            v-model="taxPayer.residential_address.street" required>
        </form-group>
      </div>

      <div class="form-row">
        <div class="form-group col">
          <label for="city">City</label>
          <input type="text" class="form-control" id="city" placeholder="City"
            v-model="taxPayer.residential_address.city" required>
        </div>
        <div class="form-group col">
          <label for="ward">Ward</label>
          <input type="text" class="form-control" id="ward" placeholder="Ward"
            v-model="taxPayer.residential_address.ward">
        </div>
        <div class="form-group col">
          <label for="lga">LGA of Residence</label>
          <input type="text" class="form-control" id="lga" placeholder="LGA of Residence"
            v-model="taxPayer.residential_address.lga" required>
        </div>
      </div>

      <div class="form-row">
        <div class="form-group col">
          <label for="state">State of Residence</label>
          <input type="text" class="form-control" id="state" placeholder="State of Residence"
            v-model="taxPayer.residential_address.state" required>
        </div>
        <div class="form-group col">
          <label for="country">Country</label>
          <select class="form-control" id="country" placeholder="Country"
            v-model="taxPayer.residential_address.country" required>
            <option v-for="country in countries" :key="country" :value="country">
              {{ country }}
            </option>
          </select>
        </div>
        <div class="form-group col">
          <label for="phone">Phone</label>
          <input type="tel" class="form-control" id="phone" placeholder="Phone"
            v-model="taxPayer.phone" required>
        </div>
      </div>

      <div class="form-row">
        <div class="form-group col">
          <label for="email">Email</label>
          <input type="email" class="form-control" id="email" placeholder="Email"
            v-model="taxPayer.email" required>
        </div>
      </div>
    </fieldset>

    <button class="btn btn-info btn-fill float-right" @click.stop="submitForm">Submit</button>
  </form>
</template>

<script>
export default {
  name: 'Individual',
  data() {
    return {
      taxPayer: {
        residential_address: {}
      },
      genderChoices: ['Male', 'Female'],
      maritalStatusChoices: ['Single', 'Married'],
      employmentStatusChoices: [
        'Unemployed', 'Self Employed', 'Employed'
      ],
      countries: ['Nigeria'],
      defaultNationality: 'Nigeria'
    }
  },
  methods: {
    submitForm(evt){
      alert(JSON.stringify(this.taxPayer))
    }
  }
}
</script>

